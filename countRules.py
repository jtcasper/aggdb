import AGG
import pubchempy as pcp

from Classes.Graph import Compound

from Rules.BondRules import RuleSet as Rules

c = pcp.Compound.from_cid(962)
water = Compound(c)

compounds = [water, Compound(pcp.Compound.from_cid(280))]

Logger = AGG.Utils.Logger.Logger()
Rules.updateLoggerInstance(Logger)

Logger.writeStr("Hello, world!")

AGG.Classes.Rule.writeCountCSV(
        "out.txt", compounds, Rules, LogTarget=Logger,
        PrintGraphs=True, FlushCSV=True)
