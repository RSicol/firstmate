import os,pathlib,subprocess,json,time,shutil,runpy
root=pathlib.Path.cwd();scratch=root/'.validation-final'
base=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX')
ev=base/'final-core-checks';old=base/'setup-continuation'
helper=root/'bin/fm-herdr-lab.sh'
env={**os.environ,'PATH':'/usr/local/bin:'+os.environ['PATH'],'FM_HERDR_LAB_STATE_DIR':str(scratch/'herdr-state'),'TMPDIR':str(scratch/'tmp')}
assert shutil.which('herdr',path=env['PATH'])=='/usr/local/bin/herdr'
assert shutil.which('gh',path=env['PATH'])=='/home/sreazy/.local/share/mise/installs/gh/latest/gh_2.102.0_linux_amd64/bin/gh'
# Reuse the existing native setup and narrow command builder. None starts a worker.
for source,dest in [('prepare-input.py','prepare-input.py'),('prefetch-command.sh','prefetch-command.sh'),('acquisition.py','acquisition.py'),('waiting-prestart.corrected-offline.py','waiting-prestart.py')]:
 text=(old/source).read_text().replace('.validation-continuation','.validation-final').replace(str(old),str(ev))
 # Bound any completed-command wait using its explicit status file, not stderr.
 # The corrected predecessor already makes these response-boundary changes.
 (scratch/dest).write_text(text)
 (ev/dest).write_text(text)

def command(args,name,timeout=30,extra_env=None):
 with (ev/name).open('w') as log:
  p=subprocess.run(args,env=extra_env or env,stdout=log,stderr=subprocess.STDOUT,timeout=timeout)
 if p.returncode:raise RuntimeError(name+': command refused or failed; no retry')
 return p

# Establish all supplied inputs before touching a live lab or doing a fetch.
command(['python3',str(scratch/'prepare-input.py')],'prepare-input.log',120,os.environ.copy())
command(['bash',str(root/'bin/fm-lab-home.sh'),'create',str(scratch/'lab-home')],'lab-home-create.log')
name=subprocess.run(['bash',str(helper),'name','start-repair-final'],env=env,capture_output=True,text=True,check=True).stdout.strip()
(scratch/'ready').write_text(name+'\n');(ev/'session-name.txt').write_text(name+'\n')
provisioned=False
try:
 command(['bash',str(helper),'provision',name],'lab-provision.log',30)
 provisioned=True
 tripwire=scratch/'herdr-state'/(name+'.fleet-state.json')
 shutil.copyfile(tripwire,ev/'default-baseline-before.json')
 command(['bash',str(helper),'run',name,'status','--json'],'lab-status.json')
 # Each positive path executes once. Any guard or native refusal stops the turn.
 command(['python3',str(scratch/'acquisition.py')],'acquisition-driver.log',150)
 command(['python3',str(scratch/'waiting-prestart.py')],'waiting-prestart-console.log',150)
 (ev/'live-driver-result.json').write_text(json.dumps({'result':'pass','live':True,'real_github_acquisition_calls':1,'new_owned_prestart_attempts':1},indent=2))
 print('Two approved live positive paths completed.',flush=True)
except Exception as e:
 (ev/'live-driver-result.json').write_text(json.dumps({'result':'blocked','reason':str(e)},indent=2))
 print('STOP: '+str(e),flush=True)
 raise
finally:
 tripwire=scratch/'herdr-state'/(name+'.fleet-state.json')
 if tripwire.exists():
  if not (ev/'default-baseline-before.json').exists():shutil.copyfile(tripwire,ev/'default-baseline-before.json')
  command(['bash',str(helper),'teardown',name],'lab-cleanup.log',40)
  p=subprocess.run(['bash',str(helper),'run',name,'session','list','--json'],env=env,capture_output=True,text=True,check=True,timeout=15)
  sessions=json.loads(p.stdout)['sessions']
  baseline=json.loads((ev/'default-baseline-before.json').read_text())
  defaults=[s for s in sessions if s.get('default') is True]
  assert len(defaults)==1,'default tripwire identity is ambiguous'
  current={k:defaults[0].get(k) for k in baseline}
  (ev/'default-baseline-after.json').write_text(json.dumps(current,indent=2))
  checks={'owned_lab_absent':not any(s.get('name')==name for s in sessions),'default_baseline_unchanged':current==baseline,'default_still_running':current.get('running') is True,'owned_tripwire_removed':not tripwire.exists()}
  (ev/'cleanup-confirmation.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks),flush=True)
  assert all(checks.values()),'guarded cleanup incomplete'
