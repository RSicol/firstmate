import os, pathlib, subprocess, json, shutil
root=pathlib.Path.cwd()
ev=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/setup-continuation')
seed=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/data/sennvora-start-repair-approval/live-acquisition-input-20261020/website-seed')
entry='/home/sreazy/.local/share/mise/installs/gh/latest/gh_2.102.0_linux_amd64/bin/gh'
identity='/home/sreazy/.local/share/mise/installs/gh/2.102.0/gh_2.102.0_linux_amd64/bin/gh'
expected={'GIT_CONFIG_COUNT':'2','GIT_CONFIG_KEY_0':'credential.helper','GIT_CONFIG_VALUE_0':'','GIT_CONFIG_KEY_1':'credential.https://github.com.helper','GIT_CONFIG_VALUE_1':'!'+entry+' auth git-credential'}
context=os.environ.copy()
checks={'existing_descriptor_conflict':any(k in context and context[k]!=v for k,v in expected.items()),'unknown_git_config_override':any(k.startswith('GIT_CONFIG') and k not in expected for k in context),'unsupported_auth_override_present':any(context.get(k) for k in ['GH_TOKEN','GITHUB_TOKEN','GH_CONFIG_DIR']) or context.get('GH_HOST','') not in ('','github.com'),'selected_entry_matches_outer':shutil.which('gh')==entry and str(pathlib.Path(entry).resolve())==identity,'supplied_seed_exists':seed.is_dir() and not seed.is_symlink()}
if checks['existing_descriptor_conflict'] or checks['unknown_git_config_override'] or checks['unsupported_auth_override_present'] or not checks['selected_entry_matches_outer'] or not checks['supplied_seed_exists']:
 (ev/'preconditions.json').write_text(json.dumps(checks,indent=2));raise SystemExit('STOP: supplied acquisition inputs do not match approved context')
context.update(expected)
checks.update({'descriptor_count_two':context['GIT_CONFIG_COUNT']=='2','descriptor_reset_helper':context['GIT_CONFIG_KEY_0']=='credential.helper' and context['GIT_CONFIG_VALUE_0']=='','descriptor_github_key':context['GIT_CONFIG_KEY_1']=='credential.https://github.com.helper','descriptor_helper_present':context['GIT_CONFIG_VALUE_1']==expected['GIT_CONFIG_VALUE_1']})
def git(cwd,*args):
 p=subprocess.run(['git','-c','core.hooksPath=/dev/null','-C',str(cwd),*args],env={**context,'GIT_OPTIONAL_LOCKS':'0'},text=True,capture_output=True)
 if p.returncode:raise RuntimeError('local Git input check failed (output withheld)')
 return p.stdout.strip()
origin='https://github.com/RSicol/sennvora-website.git'
checks.update({'seed_expected_origin':git(seed,'remote','get-url','origin')==origin,'seed_expected_head':git(seed,'rev-parse','HEAD')=='06eea5f95641a78d8eaa0b220ca30a7a50a431d4','seed_clean':not git(seed,'status','--porcelain'),'seed_ordinary_clone':(seed/'.git').is_dir() and not (seed/'.git').is_symlink() and not (seed/'.git/objects/info/alternates').exists()})
(ev/'preconditions.json').write_text(json.dumps(checks,indent=2))
assert all(checks[k] for k in ['seed_expected_origin','seed_expected_head','seed_clean','seed_ordinary_clone'])
project=root/'.validation-continuation/website'
assert not project.exists() and not project.is_symlink()
p=subprocess.run(['git','-c','core.hooksPath=/dev/null','clone','--local','--no-hardlinks','--template=',str(seed),str(project)],env=context,capture_output=True,text=True)
assert p.returncode==0,'local bootstrap clone failed (output withheld)'
git(project,'remote','set-url','origin',origin)
assert not (project/'.git/objects/info/alternates').exists()
# Keep the emitted expected-root metadata private in scratch; never log it.
p=subprocess.run(['bash','.validation-continuation/prefetch-command.sh',str(project)],env=context,capture_output=True,text=True)
assert p.returncode==0,'native command builder refused the context (values withheld)'
(root/'.validation-continuation/prefetch-command').write_text(p.stdout)
checks['command_generated_before_acquire']=True
checks['test_input_copy_in_worktree']=True
checks['seed_unchanged_after_copy']=git(seed,'rev-parse','HEAD')=='06eea5f95641a78d8eaa0b220ca30a7a50a431d4' and not git(seed,'status','--porcelain')
(ev/'preconditions.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
print('Own copy prepared locally; no external acquisition or authentication probe performed.')
