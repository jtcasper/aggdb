import AGG
import AGG.Classes.Constraint as ConstraintMod
import AGG.Classes.GraphClass.BaseGraphClass as BaseGraphClass
import AGG.Classes.Rule as RuleMod

# -----------------------------------------------
# Access the types.
# -----------------------------------------------

TypeAcc = ConstraintMod.TypeAccessor(Ontology)


#--------------------------
# Define Ruleset
#--------------------------

RuleSet = RuleMod.RuleSet("BondRules")

#--------------------------
# Define Constraints
#--------------------------

#TODO Make an Ontology. This is starting to make sense. Use HandRules and SciIntro_ontology.

Hydrogren_Constraint = ConstraintMod.UnaryValueOrConstraint(
    Ontology, "str==", TypeAcc, ConstraintMod.Value.compile(Ontology, "atom", "hydrogen")
)

#--------------------------
# R01 has Hydrogen atom
#--------------------------
R01_Comment = \
"""
This rule tests for the existence of a hydrogen atom in the compound.
"""

R01_Class = BaseGraphClass(Ontology)
R01_Class.addGroundNode( "c", UnaryConstraints=[Hydrogen_Constraint])

R01 =