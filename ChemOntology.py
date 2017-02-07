import AGG
from AGG.Classes.Ontology import *
from AGG.Classes.Ontology.ElementType import *

# ================================================
# Ontology Definition.
# ================================================

# --------------------------------------------
# Set the name.
# --------------------------------------------
Name = "Chem Ontology"


# --------------------------------------------
# Set Field Types.
# --------------------------------------------

FieldTypes = FieldType.BASE_TYPES.values()

# --------------------------------------------
# Load the known comparisons.
# --------------------------------------------

Comparisons = Comparison.Comparisons.values()

# --------------------------------------------
# Import Functions.
# --------------------------------------------

Functions = [\
    Function.CollectWords,
    Function.CollectLastNonemptyChar]


# --------------------------------------------
# Define the associated Node Types.
# --------------------------------------------

ElementNode = NodeType(
    "atom"#,
    #RequiredFields=[ElementTypeField("1", FieldType.StringType)]
    )

# CarbonAtom = NodeType(
#     "carbon",
#     RequiredFields=[ElementTypeField("6", FieldType.StringType)]
# )

NodeTypes = [ElementNode]

# --------------------------------------------
# Map Fields.
# --------------------------------------------

MapAuth = ElementTypeField("SubmittingAuthorID", FieldType.StringType)

# print MapAuth.toString()

GraphFields = [MapAuth]

# --------------------------------------------
# Define the associated Arc Types.
# --------------------------------------------

SingleBond = ArcType(
    "1", Directed=False#,
    #RequiredFields=[\
    #    ElementTypeField("1", FieldType.StringType)]
    )

DoubleBond = ArcType(
    "2", Directed=False#,
    #RequiredFields=[\
        #ElementTypeField("2", FieldType.StringType)]
        )

ArcTypes = [SingleBond, DoubleBond]

# --------------------------------------------
# Define the Ontology.
# --------------------------------------------



ChemOntology = Ontology.Ontology(
    Name,
    FieldTypes,
    Comparisons,
    Functions,
    NodeTypes,
    ArcTypes,
    GraphFields)
