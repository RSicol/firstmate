import os,pathlib,subprocess,json,time
root=pathlib.Path.cwd();scratch=root/'.validation-final'
ev=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/final-core-checks')
fish='/home/sreazy/sennvora/arbeitsbereich/secondmate-website/data/sennvora-start-repair-approval/fish-runtime/4.9.3/bin'
env={**os.environ,'PATH':fish+':'+os.environ['PATH'],'TMPDIR':str(scratch/'tmp')}
results=[]
for name in ['fm-spawn-github-prefetch','fm-control-prestart','fm-control','fm-spawn-worktree-settle']:
 start=time.monotonic()
 with (ev/(name+'.log')).open('w') as log:
  p=subprocess.run(['timeout','300','bash','tests/'+name+'.test.sh'],env=env,stdout=log,stderr=subprocess.STDOUT)
 result={'test':'bash tests/'+name+'.test.sh','exit':p.returncode,'seconds':round(time.monotonic()-start,1),'live':False}
 results.append(result);print(json.dumps(result),flush=True)
 (ev/'regression-results.json').write_text(json.dumps(results,indent=2))
 if p.returncode:raise SystemExit(p.returncode)
