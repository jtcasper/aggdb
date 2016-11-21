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

for a, value in water.getNodes().items():
#    n = Node(a.aid, a.element, a.x, a.y)
    pp.pprint(value.getElement())
    pp.pprint(value.getID())
    for pos, bond in value.getArcs().items():
        pp.pprint(pos)
        pp.pprint(bond.getAtom_ID2())

for b, value in water.getArcs().items():
#    a = Bond(b.aid1, b.aid2, b.order)
    pp.pprint(value.getNodes())
    pp.pprint(value.getOrder())

Logger = AGG.Utils.Logger.Logger()
Rules.updateLoggerInstance(Logger)

Logger.writeStr("Hello, world!")

AGG.Classes.Rule.writeCountCSV(
        "out.txt", compounds, Rules, LogTarget=Logger,
        PrintGraphs=True, FlushCSV=True)
