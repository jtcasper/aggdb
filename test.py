import pubchempy as pcp
import pprint as pp
#from Classes.Bond import Bond
from Classes.Node import Node
from Classes.Bond import Bond

c = pcp.Compound.from_cid(962)
pp.pprint(c.atoms)
pp.pprint(c.bonds)

for a in c.atoms:
    n = Node(a.aid, a.element, a.x, a.y)
    pp.pprint(n.getElement())
    pp.pprint(n.agg_getID())

for b in c.bonds:
    a = Bond(b.aid1, b.aid2, b.order)
    pp.pprint(a.getAtoms())
    pp.pprint((a.getOrder()))