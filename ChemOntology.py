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

HydrogenAtom = NodeType(
    "citation",
    RequiredFields=[ElementTypeField("1", FieldType.StringType)])

NodeTypes = [HydrogenAtom]

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
    "Single", Directed=False,
    RequiredFields=[\
        ElementTypeField("1", FieldType.StringType)])

ArcTypes = [SingleBond]

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
