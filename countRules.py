import AGG
import pubchempy as pcp

from Classes.Graph import Compound

from Rules.BondRules import RuleSet as Rules

c = pcp.Compound.from_cid(962)
water = Compound(c)
ethanol = Compound(pcp.Compound.from_cid(702))

compounds = [#water, Compound(pcp.Compound.from_cid(280)),
 ethanol]

Logger = AGG.Utils.Logger.Logger()
Rules.updateLoggerInstance(Logger)

AGG.Classes.Rule.writeCountCSV(
    "out.txt", compounds, Rules, LogTarget=Logger,
     PrintGraphs=True, FlushCSV=True)
