"""
The Node class represents the elements of a compound as nodes.
"""

import AGG

class Node(AGG.Classes.API.Node):

    def __init__(self, atom_ID, element, xpos=0, ypos=0):

        self.atom_ID = atom_ID
        self.element = element
        self.xpos = xpos
        self.ypos = ypos
        self.bonds = []

    #----------------------
    # Node Accessors
    #----------------------

    def getXPos(self):
        """
        Get the X Position of Node
        :return:
        """
        return self.xpos

    def getYPos(self):
        """
        Get the Y Position of Node
        :return:
        """
        return self.ypos

    def getElement(self):
        """
        Return the element by atomic number
        :return:
        """
        return self.element

    def getID(self):
        """
        Return the atom id of this atom
        :return:
        """
        return self.atom_ID

    def getArcs(self):
        """
        Return the bond dictionary of this atom
        :return:
        """
        return self.bonds

    #----------------------
    # Bond Addition
    #----------------------

    def addBond(self, bond):
        """
        Adds bond to bond dictionary
        :param bond: A bond dictionary with atom_id2, atom_id1, and bond type
        """
        self.bonds.append(bond)

    #----------------------
    # Portability
    #----------------------
    #no longer needed as now stored in list rather than dict in graph
    def toDict(self):
        """
        Return a version of itself as a dictionary
        :return:
        """
        return {self.getID(): self}


    #------------------
    # Debug
    #------------------
    def __str__(self):
        return "Node ID: {}, Element: {}".format(self.getID(), self.getElement())

    def __repr__(self):
        return self.__str__()

    #----------------------
    # API Interface methods
    #----------------------

    def agg_getID(self):
        """
        Get the identifier for the node.

        This is the aid generated when the compound is pulled from
        PubChem.
        """
        return self.getID()

    def agg_getArcs(self):
        """
        Returns the bonds between this atom and other atoms
        """
        return self.getArcs()

    def agg_getInboundArcs(self):
        """
        Not meaningful as all arcs are bidirectional
        """
        raise AGG.Classes.API.APIError.APIError, "All arcs are bidirectional."

    def agg_getOutboundArcs(self):
        """
        Not meaningful as all arcs are bidirectional
        """
        raise AGG.Classes.API.APIError.APIError, "All arcs are bidirectional."

    def agg_getType(self):
        """
        Get the type of this arc as per the ontology
        set in the system.
        """
        return str(self.getElement())

    def agg_getField(self, FieldName, Subfield=None):
        """
        Interface method for retreival of the field
        items if they are present.
        """
        raise AGG.Classes.API.APIError.APIError, "Unimplemented Stub."

    def agg_hasField(self, FieldName, Subfield=None):
        """
        Return True if the named field/subfield is present.
        """
        raise AGG.Classes.API.APIError.APIError, "Unimplemented Stub."


    def agg_listFields(self):
        """
        Interface method to list known fields.
        """
        raise AGG.Classes.API.APIError.APIError, "Unimplemented Stub."


    def agg_listSubfields(self, FieldName):
        """
        Interface method to list subfields of named field.
        """
        raise AGG.Classes.API.APIError.APIError, "Unimplemented Stub."
