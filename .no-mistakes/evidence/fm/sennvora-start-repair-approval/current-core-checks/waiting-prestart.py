import os, pathlib, subprocess, json, time, threading, socket, shlex
root=pathlib.Path.cwd()
ev=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/current-core-checks')
lab=root/'.validation-current/lab-home'; project=lab/'projects/app'
session=(root/'.validation-current/ready').read_text().strip()
env=os.environ.copy(); env['PATH']='/usr/local/bin:'+env['PATH']; env['FM_HERDR_LAB_STATE_DIR']=str(root/'.validation-current/herdr-state')
helper=root/'bin/fm-herdr-lab.sh'
log=(ev/'waiting-prestart-driver.log').open('w',buffering=1)
def run(args,cwd=root,timeout=15,custom=None):
 r=subprocess.run(args,cwd=cwd,env=custom or env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
 log.write('$ '+shlex.join(map(str,args))+'\n'+r.stdout+r.stderr+'\nexit='+str(r.returncode)+'\n')
 if r.returncode: raise RuntimeError('command refused or failed; see driver log')
 return r.stdout

def herdr(*args):return json.loads(run(['bash',str(helper),'run',session,*map(str,args)]))
stop=threading.Event(); listener=socket.socket(); listener.bind(('127.0.0.1',0));listener.listen();listener.settimeout(.2)
port=listener.getsockname()[1]; connections=[]
def wait_https():
 # Deliberately withhold the TLS handshake, never accept an unverified certificate.
 while not stop.is_set():
  try:
   connection,address=listener.accept();connections.append(connection)
   log.write('own loopback HTTPS connection accepted; withholding TLS response\n')
  except socket.timeout:pass
  except OSError:break
thread=threading.Thread(target=wait_https,daemon=True);thread.start()
try:
 (lab/'.tasks.toml').write_text('backend = "markdown"\n[markdown]\npath = "data/backlog.md"\narchive = "data/done-archive.md"\ndone_keep = 10\n')
 (lab/'data/backlog.md').write_text('# Backlog\n')
 (lab/'config/backend').write_text('herdr\n')
 task='sennvora-start-repair-approval'
 run(['tasks-axi','add',task,'Own disposable waiting HTTPS prestart','--kind','scout','--repo','app','--json'],cwd=lab)
 run(['tasks-axi','hold',task,'--reason','Controlled own lab prestart cancellation check','--kind','captain','--json'],cwd=lab)
 project.mkdir();run(['git','init','--template=','--initial-branch=main',str(project)])
 (project/'README.md').write_text('Own controlled cancellation lab; no production data.\n')
 run(['git','add','README.md'],cwd=project)
 run(['git','-c','core.hooksPath=/dev/null','-c','user.name=Lab Test','-c','user.email=lab@example.invalid','commit','-qm','Own lab seed'],cwd=project)
 origin=f'https://127.0.0.1:{port}/own.git'
 run(['git','remote','add','origin',origin],cwd=project)
 before=run(['git','rev-parse','HEAD'],cwd=project).strip()
 ws=herdr('workspace','create','--cwd',lab,'--label','own-start-repair','--no-focus')
 (ev/'workspace-created.json').write_text(json.dumps(ws,indent=2))
 w=ws['result']['workspace'];wid=w['workspace_id']
 # The create response owns the seeded actor identity; do not discover by label.
 tabs=herdr('tab','list','--workspace',wid)
 (ev/'own-tabs.json').write_text(json.dumps(tabs,indent=2))
 assert len(tabs['result']['tabs'])==1
 actor_tab=tabs['result']['tabs'][0]['tab_id']
 panes=herdr('pane','list','--workspace',wid)
 (ev/'own-panes-created.json').write_text(json.dumps(panes,indent=2))
 actor=next(p['pane_id'] for p in panes['result']['panes'] if p['tab_id']==actor_tab)
 target=herdr('tab','create','--workspace',wid,'--cwd',project,'--label','fm-'+task,'--no-focus')
 (ev/'target-created.json').write_text(json.dumps(target,indent=2))
 # Inspect only this creation response and the exact newly created tab.
 tab=target['result']['tab'];tid=tab['tab_id']
 pane=target['result']['root_pane']['pane_id']
 cmd=shlex.join(['env','TREEHOUSE_ROOT='+str(lab/'pool'),'GIT_TERMINAL_PROMPT=0','GIT_ASKPASS=/bin/false','treehouse','get'])
 herdr('pane','run',pane,cmd)
 for n in range(60):
  info=herdr('pane','process-info','--pane',pane)
  processes=info.get('result',{}).get('process_info',{}).get('foreground_processes',[])
  if len(processes)>=3 and any(p.get('name')=='git' for p in processes) and connections:break
  time.sleep(.2)
 else:raise RuntimeError('own Treehouse/Git waiting process tree did not converge')
 (ev/'waiting-process-info.json').write_text(json.dumps(info,indent=2))
 control=root/'.validation-current/control-from-actor.sh'
 control.write_text('#!/usr/bin/env bash\nset -eu\n'+
  'cd '+shlex.quote(str(lab))+'\n'+
  'env -u FM_ROOT_OVERRIDE -u FM_STATE_OVERRIDE -u FM_DATA_OVERRIDE -u FM_CONFIG_OVERRIDE -u FM_PROJECTS_OVERRIDE FM_HOME='+shlex.quote(str(lab))+' '+shlex.quote(str(root/'bin/fm-control.sh'))+' '+task+' cancel-prestart --pane '+shlex.quote(pane)+' > '+shlex.quote(str(ev/'fresh-snapshot.json'))+' 2> '+shlex.quote(str(ev/'inspection-errors.log'))+'\n'+
  'touch '+shlex.quote(str(root/'.validation-current/inspected'))+'\n')
 herdr('pane','run',actor,shlex.join(['bash',str(control)]))
 for n in range(100):
  if (root/'.validation-current/inspected').exists():break
  if (ev/'inspection-errors.log').exists() and (ev/'inspection-errors.log').stat().st_size:raise RuntimeError('native inspection refused; no retry or input')
  time.sleep(.2)
 else:raise RuntimeError('inspection did not finish')
 snapshot=json.loads((ev/'fresh-snapshot.json').read_text());assert snapshot['input_sent'] is False
 # Observe the same live processes after read-only inspection.
 after_inspection=herdr('pane','process-info','--pane',pane)
 (ev/'process-info-after-inspection.json').write_text(json.dumps(after_inspection,indent=2))
 assert snapshot['pane']==pane and snapshot['session']==session and snapshot['home']==str(lab)
 proof=snapshot['proof']
 cancel=root/'.validation-current/cancel-from-actor.sh'
 cancel.write_text('#!/usr/bin/env bash\nset -u\ncd '+shlex.quote(str(lab))+'\n'+
  'env -u FM_ROOT_OVERRIDE -u FM_STATE_OVERRIDE -u FM_DATA_OVERRIDE -u FM_CONFIG_OVERRIDE -u FM_PROJECTS_OVERRIDE FM_HOME='+shlex.quote(str(lab))+' '+shlex.quote(str(root/'bin/fm-control.sh'))+' '+task+' cancel-prestart --pane '+shlex.quote(pane)+' --if-match '+shlex.quote(proof)+' > '+shlex.quote(str(ev/'cancel-result.log'))+' 2>&1\n'+
  'printf "%s\\n" "$?" > '+shlex.quote(str(root/'.validation-current/cancel-status'))+'\n')
 herdr('pane','run',actor,shlex.join(['bash',str(cancel)]))
 for n in range(200):
  if (root/'.validation-current/cancel-status').exists():break
  time.sleep(.2)
 else:raise RuntimeError('native cancellation did not finish; do not send more input')
 status=(root/'.validation-current/cancel-status').read_text().strip();assert status=='0', 'native cancellation failed'
 preserved=herdr('pane','get',pane);(ev/'preserved-pane.json').write_text(json.dumps(preserved,indent=2))
 stopped=herdr('pane','process-info','--pane',pane);(ev/'stopped-process-info.json').write_text(json.dumps(stopped,indent=2))
 assert run(['git','rev-parse','HEAD'],cwd=project).strip()==before
 assert not run(['git','status','--porcelain'],cwd=project).strip()
 assert not (lab/'state'/f'{task}.meta').exists()
 (ev/'waiting-prestart-result.json').write_text(json.dumps({'result':'pass','live':True,'session':session,'actor':actor,'pane':pane,'inspection_input_sent':False,'matching_cancel_calls':1,'cancel_exit':0,'project_head_unchanged':True,'project_clean':True,'endpoint_preserved':True,'metadata_not_adopted':True},indent=2))
 print('own waiting prestart: PASS')
except Exception as e:
 log.write('STOP: '+str(e)+'\n')
 (ev/'waiting-prestart-result.json').write_text(json.dumps({'result':'blocked','live':False,'reason':str(e)},indent=2))
 print('STOP:',e)
finally:
 stop.set();listener.close()
 for c in connections:c.close()
 thread.join(timeout=2)
 (root/'.validation-current/finish').touch()
 log.close()
