from pathlib import Path
import re,sys
SECRET=[re.compile(r'-----BEGIN .*PRIVATE KEY-----'),re.compile(r'gh[pousr]_[A-Za-z0-9_]{20,}'),re.compile(r'AKIA[0-9A-Z]{16}')]
FORBIDDEN={'.env','.DS_Store','Thumbs.db'}
def gate(root):
 fails=[]
 for p in Path(root).rglob('*'):
  if not p.is_file() or '.git' in p.parts:continue
  rel=str(p.relative_to(root))
  if p.name in FORBIDDEN:fails.append((rel,'forbidden file'))
  if p.stat().st_size>25_000_000:fails.append((rel,'large file >25MB'))
  if p.suffix.lower() in {'.md','.py','.js','.json','.yml','.yaml','.html','.txt'}:
   t=p.read_text(encoding='utf-8',errors='ignore')
   if any(rx.search(t) for rx in SECRET):fails.append((rel,'possible secret'))
 return fails
if __name__=='__main__':
 f=gate(sys.argv[1] if len(sys.argv)>1 else '.'); print('PASS' if not f else 'FAIL'); [print(x) for x in f]; raise SystemExit(bool(f))
