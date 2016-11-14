import pubchempy as pcp
import pprint as pp

from Classes.Node import Node
from Classes.Bond import Bond
from Classes.Graph import Compound

c = pcp.Compound.from_cid(962)
pp.pprint(c.atoms)
pp.pprint(c.bonds)

water = Compound()

water.addAtoms(c)
water.addBonds(c)

for a, value in water.getAtoms().items():
#    n = Node(a.aid, a.element, a.x, a.y)
    pp.pprint(value.getElement())
    pp.pprint(value.getID())

for b, value in water.getBonds().items():
#    a = Bond(b.aid1, b.aid2, b.order)
    pp.pprint(value.getAtoms())
    pp.pprint(value.getOrder())