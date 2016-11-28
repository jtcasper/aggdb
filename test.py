import AGG
import pubchempy as pcp
import pprint as pp

from Classes.Node import Node
from Classes.Bond import Bond
from Classes.Graph import Compound

from Rules.BondRules import RuleSet as Rules

c = pcp.Compound.from_cid(962)
pp.pprint(c)
pp.pprint(c.atoms)
pp.pprint(c.bonds)
water = Compound(c)

compounds = [water, Compound(pcp.Compound.from_cid(280))]

#water.addAtoms(c)
#water.addBonds(c)

for a in water.getNodes():
#    n = Node(a.aid, a.element, a.x, a.y)
    pp.pprint(a.getElement())
    pp.pprint(a.getID())
    for bond in a.getArcs():
        pp.pprint(bond.getNodes())

for b in water.getArcs():
#    a = Bond(b.aid1, b.aid2, b.order)
    pp.pprint(b.getNodes())
    pp.pprint(b.getOrder())

Logger = AGG.Utils.Logger.Logger()
Rules.updateLoggerInstance(Logger)

Logger.writeStr("Hello, world!")

#AGG.Classes.Rule.writeCountCSV(
#        "out.txt", compounds, Rules, LogTarget=Logger,
#        PrintGraphs=True, FlushCSV=True)
