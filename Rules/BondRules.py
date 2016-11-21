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