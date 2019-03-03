import sys, os
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p)
from Equipment import equipment as eq

e =  eq.Equipment("st01")
print(e.name)