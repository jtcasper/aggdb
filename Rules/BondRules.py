import AGG
import AGG.Classes.Constraint as ConstraintMod
import AGG.Classes.GraphClass.ExtendedGraphClass as ExtendedGraphClass
import AGG.Classes.Rule as RuleMod

from ChemOntology import ChemOntology


# -----------------------------------------------
# Access the types.
# -----------------------------------------------

TypeAcc = ConstraintMod.TypeAccessor(ChemOntology)


#--------------------------
# Define Ruleset
#--------------------------

RuleSet = RuleMod.RuleSet("BondRules")

#--------------------------
# Define Constraints
#--------------------------

#TODO Make an Ontology. This is starting to make sense. Use HandRules and SciIntro_ontology.

Hydrogen_Constraint = ConstraintMod.UnaryValueOrConstraint(
    ChemOntology, "str==", TypeAcc, ConstraintMod.Value.compile(ChemOntology, "String", "1")
)

Carbon_Constraint = ConstraintMod.UnaryValueOrConstraint(
    ChemOntology, "str==", TypeAcc, ConstraintMod.Value.compile(ChemOntology, "String", "6")
)

Oxygen_Constraint = ConstraintMod.UnaryValueOrConstraint(
    ChemOntology, "str==", TypeAcc, ConstraintMod.Value.compile(ChemOntology, "String", "8")
)

Single_Bond_Constraint = ConstraintMod.UnaryValueOrConstraint(
    ChemOntology, "str==", TypeAcc, ConstraintMod.Value.compile(ChemOntology, "String", "1")
)

Double_Bond_Constraint = ConstraintMod.UnaryValueOrConstraint(
    ChemOntology, "str==", TypeAcc, ConstraintMod.Value.compile(ChemOntology, "String", "2")
)


#--------------------------
# R01 has Hydrogen atom
#--------------------------
R01_Comment = \
"""
This rule tests for the existence of a hydrogen atom in the compound.
"""

R01_Class = ExtendedGraphClass(ChemOntology)
R01_Class.addGroundNode( "c", UnaryConstraints=[Hydrogen_Constraint])

R01 = RuleSet.addRule("R01_hasHydrogen", R01_Class, Comment=R01_Comment)

#--------------------------
# R02 has Carbon atom
#--------------------------
R02_Comment = \
"""
This rule tests for the existence of a carbon atom in the compound.
"""

R02_Class = ExtendedGraphClass(ChemOntology)
R02_Class.addGroundNode( "c", UnaryConstraints=[Carbon_Constraint])

R02 = RuleSet.addRule("R02_hasCarbon", R02_Class, Comment=R02_Comment)

#--------------------------
# R03 has a single bond
#--------------------------
R03_Comment = \
"""
This rule tests for the existence of a single bond in the compound.
"""

R03_Class = ExtendedGraphClass(ChemOntology)
R03_Class.addGroundNode("s")
R03_Class.addGroundNode("f")
R03_Class.addGroundArc("b", "undirected", "s", "f", UnaryConstraints=[Single_Bond_Constraint])


R03 = RuleSet.addRule("R03_hasSingleBond", R03_Class, Comment=R03_Comment)

#--------------------------
# R04 has a double bond
#--------------------------
R04_Comment = \
"""
This rule tests for the existence of a double bond in the compound.
"""

R04_Class = ExtendedGraphClass(ChemOntology)
R04_Class.addGroundNode("s")
R04_Class.addGroundNode("f")
R04_Class.addGroundArc("b", "undirected", "s", "f", UnaryConstraints=[Double_Bond_Constraint])


R04 = RuleSet.addRule("R04_hasDoubleBond", R04_Class, Comment=R04_Comment)

#--------------------------
# R05 has a hydroxyl group
#--------------------------
R05_Comment = \
"""
This rule tests for the existence of a hydroxyl group in the compound.
"""

R05_Class = ExtendedGraphClass(ChemOntology)
R05_Class.addGroundNode("r", UnaryConstraints=[Carbon_Constraint])
R05_Class.addGroundNode("o", UnaryConstraints=[Oxygen_Constraint])
R05_Class.addGroundNode("h", UnaryConstraints=[Hydrogen_Constraint])
R05_Class.addGroundArc("r_group", "undirected", "r", "o", UnaryConstraints=[Single_Bond_Constraint])
R05_Class.addGroundArc("hydroxyl_group", "undirected", "o", "h", UnaryConstraints=[Single_Bond_Constraint])

R05 = RuleSet.addRule("R05_hasHydroxylGroup", R05_Class, Comment=R05_Comment)
