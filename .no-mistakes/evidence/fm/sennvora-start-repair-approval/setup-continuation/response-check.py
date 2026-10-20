import io,json,pathlib,subprocess,os,shlex,time
root=pathlib.Path.cwd();scratch=root/'.validation-continuation'
ev=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/setup-continuation')
original=pathlib.Path('/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/current-core-checks/waiting-prestart.py').read_text()
attempted=(ev/'waiting-prestart.py').read_text();corrected=(scratch/'waiting-prestart.py').read_text()
# Execute only the actual response-handling sections: never rerun live setup.
# Assertions below concern outputs, exceptions and completed command exit status.
def response_namespace(source):
 ns={'json':json,'run':lambda *a,**kw:'','helper':pathlib.Path('unused'),'session':'synthetic'}
 section=source[source.index('def herdr('):source.index('stop=threading.Event()')]
 exec(compile(section,'driver-response','exec'),ns)
 return ns
try:response_namespace(original)['herdr']('pane','run','own','true')
except json.JSONDecodeError:print('REPRODUCED: original driver parses successful empty response as JSON')
else:raise AssertionError('original parser failure not reproduced')
ns=response_namespace(corrected)
assert ns['herdr']('pane','run','own','true')==''
ns['run']=lambda *a,**kw:'{"result":{"type":"metadata"}}'
assert ns['herdr']('pane','get','own')['result']['type']=='metadata'
ns['run']=lambda *a,**kw:'invalid-json'
try:ns['herdr']('pane','get','own')
except json.JSONDecodeError:pass
else:raise AssertionError('invalid metadata was accepted')
def fail(*a,**kw):raise RuntimeError('synthetic exit 7')
ns['run']=fail
try:ns['herdr']('pane','run','own','false')
except RuntimeError:pass
else:raise AssertionError('failed command was accepted')
print('PASS: empty command success, valid metadata, malformed metadata and command failure')

def inspect_case(name,source,code=0,body='{"input_sent":false}',expect=None):
 case=scratch/'response-fixtures'/name;case.mkdir(parents=True)
 (case/'.validation-continuation').mkdir();(case/'bin').mkdir();(case/'lab').mkdir();(case/'evidence').mkdir()
 mock=case/'bin/fm-control.sh'
 mock.write_text('#!/usr/bin/env bash\nprintf "informational diagnostic\\n" >&2\nsleep .6\nprintf "%s\\n" '+shlex.quote(body)+'\nexit '+str(code)+'\n');mock.chmod(0o700)
 children=[]
 def submit(*args):
  children.append(subprocess.Popen(shlex.split(args[3]),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL))
  return ''
 ns={'root':case,'lab':case/'lab','ev':case/'evidence','task':'synthetic','pane':'own','actor':'actor','herdr':submit,'shlex':shlex,'time':time,'json':json}
 section=source[source.index(' control=root/'):source.index(' # Observe the same live processes')]
 error=None
 try:exec(compile('if True:\n'+section,'driver-inspection','exec'),ns)
 except Exception as e:error=e
 finally:
  for child in children:child.wait(timeout=5)
 if expect is None:
  assert error is None,repr(error)
  assert ns['snapshot']['input_sent'] is False
 else:assert isinstance(error,expect),repr(error)
 print('PASS: '+name)
inspect_case('prior-premature-stderr-reproduced',attempted,expect=RuntimeError)
inspect_case('corrected-waits-for-success-despite-stderr',corrected)
inspect_case('nonzero-inspection-remains-failure',corrected,code=7,body='',expect=AssertionError)
inspect_case('malformed-inspection-remains-failure',corrected,body='not-json',expect=json.JSONDecodeError)
print('All focused response-contract checks passed; no real Herdr or authentication operation.')
