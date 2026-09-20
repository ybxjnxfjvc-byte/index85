import tempfile,unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
from repo_gate import gate
class T(unittest.TestCase):
 def test_env_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/'.env').write_text('x=1'); self.assertTrue(gate(p))
 def test_clean(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/'README.md').write_text('ok'); self.assertFalse(gate(p))
if __name__=='__main__':unittest.main()
