import os,pathlib,subprocess,json,time,shlex
root=pathlib.Path.cwd();scratch=root/'.validation-final'
ev=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/final-core-checks')
session=(scratch/'ready').read_text().strip();project=scratch/'website';pool=scratch/'website-pool';trace=scratch/'native-fetch-trace.jsonl'
helper=root/'bin/fm-herdr-lab.sh';env=os.environ.copy();env['PATH']='/usr/local/bin:'+env['PATH'];env['FM_HERDR_LAB_STATE_DIR']=str(scratch/'herdr-state')
entry='/home/sreazy/.local/share/mise/installs/gh/latest/gh_2.102.0_linux_amd64/bin/gh'
resolved='/home/sreazy/.local/share/mise/installs/gh/2.102.0/gh_2.102.0_linux_amd64/bin/gh'
def herdr(*args):
 p=subprocess.run(['bash',str(helper),'run',session,*map(str,args)],env=env,text=True,capture_output=True,timeout=15)
 if p.returncode:raise RuntimeError('guarded Herdr operation refused; output withheld; no retry')
 return p.stdout if args[:2]==('pane','run') else json.loads(p.stdout)
def git(cwd,*args):
 p=subprocess.run(['git','-C',str(cwd),*args],env={**env,'GIT_OPTIONAL_LOCKS':'0'},text=True,capture_output=True,timeout=15)
 if p.returncode:raise RuntimeError('own acquired Git metadata check failed; output withheld')
 return p.stdout.strip()
def events():
 result=[]
 if trace.exists():
  for line in trace.read_text().splitlines():
   try:result.append(json.loads(line))
   except json.JSONDecodeError:pass # Native trace can end in an in-progress write while polling.
 return result
try:
 ws=herdr('workspace','create','--cwd',project,'--label','own-native-acquisition','--no-focus')
 pane=ws['result']['root_pane']['pane_id'];wid=ws['result']['workspace']['workspace_id']
 initial=herdr('pane','process-info','--pane',pane)['result']['process_info']
 script=scratch/'acquire-in-destination.shell'
 script.write_text('export TREEHOUSE_ROOT='+shlex.quote(str(pool))+'\nexport GIT_TRACE2_EVENT='+shlex.quote(str(trace))+'\n'+(scratch/'prefetch-command').read_text()+'\nprintf "returned\\n" > '+shlex.quote(str(scratch/'acquisition-returned'))+'\n')
 # source is evaluated by the ORIGINAL destination shell, not a new controller.
 accepted=herdr('pane','run',pane,'source '+shlex.quote(str(script)))
 assert not accepted.strip(),'pane run returned an unexpected body'
 for attempt in range(180):
  p=herdr('pane','get',pane)['result']['pane'];cwd=pathlib.Path(p['foreground_cwd'])
  data=events()
  fetches=[e['sid'] for e in data if e.get('event')=='start' and [pathlib.Path(x).name if i==0 else x for i,x in enumerate(e.get('argv',[]))]==['git','fetch','origin']]
  exits=[e for e in data if e.get('event')=='exit' and e.get('sid') in fetches]
  if any(e.get('code')!=0 for e in exits):raise RuntimeError('native Treehouse-owned Git fetch failed; no retry; auth output withheld')
  if cwd!=project and cwd.is_relative_to(pool) and (cwd/'.git').is_file() and exits:break
  if (scratch/'acquisition-returned').exists():raise RuntimeError('destination command returned without entering an acquired shell; no retry')
  time.sleep(.5)
 else:raise RuntimeError('single native acquisition did not reach an acquired shell within 90 seconds; no retry')
 final=herdr('pane','process-info','--pane',pane)['result']['process_info']
 helper_calls=[e for e in data if e.get('event')=='child_start' and 'auth git-credential' in ' '.join(e.get('argv',[]))]
 selected_helper=any(entry in ' '.join(e.get('argv',[])) or resolved in ' '.join(e.get('argv',[])) for e in helper_calls)
 assert len(fetches)==1 and len(exits)==1 and exits[0]['code']==0,'native fetch identity or exit ambiguous'
 assert selected_helper,'native selected credential helper was not observed in Git child metadata'
 assert initial['shell_pid']==final['shell_pid'],'original destination shell changed'
 common=git(cwd,'rev-parse','--git-common-dir')
 assert (cwd/common).resolve()==project/'.git','acquisition escaped own copy'
 head=git(cwd,'rev-parse','HEAD');remote_head=git(project,'rev-parse','refs/remotes/origin/HEAD')
 assert head==remote_head,'acquired checkout is not the fetched default head'
 result={'result':'pass','live':True,'native_task':'sennvora-start-repair-approval','session':session,'workspace':wid,'pane':pane,'pane_run_exit':0,'pane_run_empty_response':True,'treehouse_owned_git_fetch_count':len(fetches),'native_fetch_exit':exits[0]['code'],'selected_native_helper_observed':True,'same_destination_shell_pid':True,'destination_entered_own_pool':True,'acquired_common_dir_is_own_copy':True,'acquired_head_matches_fetched_default':True,'acquired_head':head,'foreground_process_names':[p.get('name') for p in final.get('foreground_processes',[])],'auth_output_archived':False,'actual_store_values_archived':False}
 (ev/'acquisition-result.json').write_text(json.dumps(result,indent=2))
 print(json.dumps(result,indent=2))
except Exception as error:
 (ev/'acquisition-result.json').write_text(json.dumps({'result':'blocked','live':False,'reason':str(error)},indent=2))
 raise
