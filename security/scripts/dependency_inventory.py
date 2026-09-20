from pathlib import Path
import json,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.'); items=[]
for p in root.rglob('package.json'):
 if 'node_modules' in p.parts:continue
 try:d=json.loads(p.read_text(encoding='utf-8'))
 except:continue
 for scope in ('dependencies','devDependencies'):
  for k,v in d.get(scope,{}).items():items.append({'file':str(p.relative_to(root)),'ecosystem':'npm','name':k,'version':v,'scope':scope})
for p in root.rglob('requirements.txt'):
 for line in p.read_text(encoding='utf-8',errors='ignore').splitlines():
  s=line.strip()
  if s and not s.startswith('#'):items.append({'file':str(p.relative_to(root)),'ecosystem':'python','requirement':s})
print(json.dumps({'format':'portfolio-dependency-inventory','components':items},ensure_ascii=False,indent=2))
