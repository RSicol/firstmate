import os,pathlib,subprocess,json
root=pathlib.Path.cwd();scratch=root/'.validation-continuation'
ev=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/setup-continuation')
session=(scratch/'ready').read_text().strip();env=os.environ.copy();env['PATH']='/usr/local/bin:'+env['PATH'];env['FM_HERDR_LAB_STATE_DIR']=str(scratch/'herdr-state')
p=subprocess.run(['bash',str(root/'bin/fm-herdr-lab.sh'),'run',session,'session','list','--json'],env=env,text=True,capture_output=True,check=True)
sessions=json.loads(p.stdout)['sessions']
baseline=json.loads((ev/'default-baseline-before.json').read_text())
defaults=[s for s in sessions if s.get('default') is True]
assert len(defaults)==1
current={k:defaults[0].get(k) for k in baseline}
(ev/'default-baseline-after.json').write_text(json.dumps(current,indent=2))
checks={'owned_lab_absent':not any(s.get('name')==session for s in sessions),'default_baseline_unchanged':current==baseline,'default_still_running':current.get('running') is True,'owned_tripwire_removed':not (scratch/'herdr-state'/f'{session}.fleet-state.json').exists(),'matching_cancel_calls':0,'real_github_acquire_calls':0,'native_inspection_refused':True}
(ev/'cleanup-confirmation.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
assert all(checks[k] for k in ['owned_lab_absent','default_baseline_unchanged','default_still_running','owned_tripwire_removed'])
