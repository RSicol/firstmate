import pathlib,json,subprocess,os,shutil
root=pathlib.Path.cwd();scratch=root/'.validation-final'
ev=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/final-core-checks')
rows=[]
for line in (scratch/'native-fetch-trace.jsonl').read_text().splitlines():
 try:rows.append(json.loads(line))
 except json.JSONDecodeError:pass
fetch=[r for r in rows if r.get('event')=='start' and r.get('argv')==['git','fetch','origin']]
assert len(fetch)==1
sid=fetch[0]['sid']
selected='/home/sreazy/.local/share/mise/installs/gh/latest/gh_2.102.0_linux_amd64/bin/gh'
resolved='/home/sreazy/.local/share/mise/installs/gh/2.102.0/gh_2.102.0_linux_amd64/bin/gh'
output=[]
for r in rows:
 if r.get('sid')!=sid:continue
 if r.get('event')=='start':
  output.append({k:r[k] for k in ['event','time','sid','argv']})
 elif r.get('event')=='child_start' and 'auth git-credential' in ' '.join(r.get('argv',[])):
  # Publish only known non-secret command metadata, never trace environments.
  command=' '.join(r['argv'])
  assert selected in command or resolved in command
  action=command.split()[-1]
  assert action in ['get','store','erase']
  output.append({'event':'child_start','time':r['time'],'sid':r['sid'],'child_id':r['child_id'],'selected_native_helper':selected,'action':action})
 elif r.get('event')=='exit':
  assert r['code']==0
  output.append({k:r[k] for k in ['event','time','sid','code']})
(ev/'native-fetch-events.json').write_text(json.dumps(output,indent=2))

snapshot=json.loads((ev/'fresh-snapshot.json').read_text())
inspected=json.loads((ev/'process-info-after-inspection.json').read_text())['result']['process_info']
stopped=json.loads((ev/'stopped-process-info.json').read_text())['result']['process_info']
checks={'snapshot_sent_no_input':snapshot['input_sent'] is False,'same_processes_still_running_after_inspection':sorted(p['pid'] for p in inspected['foreground_processes'])==sorted(p['pid'] for p in snapshot['processes']),'original_terminal_shell_preserved':stopped['shell_pid']==snapshot['shell'],'only_original_shell_after_cancellation':[p['pid'] for p in stopped['foreground_processes']]==[snapshot['shell']],'inspection_exit_zero':(scratch/'inspection-status').read_text().strip()=='0','cancellation_exit_zero':(scratch/'cancel-status').read_text().strip()=='0'}
assert all(checks.values())
(ev/'prestart-postconditions.json').write_text(json.dumps(checks,indent=2))
seed=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/data/sennvora-start-repair-approval/live-acquisition-input-20261020/website-seed')
def git(*a):
 p=subprocess.run(['git','-C',str(seed),*a],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'},capture_output=True,text=True,check=True)
 return p.stdout.strip()
seed_checks={'supplied_seed_head_unchanged':git('rev-parse','HEAD')=='06eea5f95641a78d8eaa0b220ca30a7a50a431d4','supplied_seed_origin_unchanged':git('remote','get-url','origin')=='https://github.com/RSicol/sennvora-website.git','supplied_seed_still_clean':not git('status','--porcelain')}
assert all(seed_checks.values())
(ev/'supplied-seed-after.json').write_text(json.dumps(seed_checks,indent=2))
for name in ['run-live.py','run-regressions.py','archive-evidence.py','control-from-actor.sh','cancel-from-actor.sh']:
 shutil.copyfile(scratch/name,ev/name)
print(json.dumps({'native_fetch_exit':0,'prestart_postconditions':checks,'seed_after':seed_checks},indent=2))
