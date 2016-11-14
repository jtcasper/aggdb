import pubchempy as pcp
import pprint as pp

from Classes.Node import Node
from Classes.Bond import Bond
from Classes.Graph import Graph

c = pcp.Compound.from_cid(962)
pp.pprint(c.atoms)
pp.pprint(c.bonds)

water = Graph()

water.addAtoms(c)
water.addBonds(c)

for a in water.getNodes():
    n = Node(a.aid, a.element, a.x, a.y)
    pp.pprint(n.getElement())
    pp.pprint(n.agg_getID())

for b in water.getBonds():
    a = Bond(b.aid1, b.aid2, b.order)
    pp.pprint(a.getAtoms())
    pp.pprint((a.getOrder()))