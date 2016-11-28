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
R03_Class.addGroundArc("b", "undirected", "s", "f")


R03 = RuleSet.addRule("R03_hasSingleBond", R03_Class, Comment=R03_Comment)
