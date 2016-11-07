"""
The Bond class represents bonds of a compound as Arcs.
"""

import AGG

class Bond(AGG.Classes.API.Arc):

    def __init__(self, atom_ID1, atom_ID2, bondOrder, ID=None):

        self.atom_ID1 = atom_ID1
        self.atom_ID2 = atom_ID2
        self.bondOrder = bondOrder
        self.ID = ID;

    #-----------------
    # Bond Accessors
    #-----------------

    def getAtoms(self):
        """
        Get both atom_ids of this bond
        """
        return (self.getAtom_ID1(), self.getAtom_ID2())

    def getAtom_ID2(self):
        """
        Get atom_ID2
        """
        return self.atom_ID2

    def getAtom_ID1(self):
        """
        Get atom_ID1
        """
        return self.atom_ID1

    def getOrder(self):
        """
        Get bond order
        :return:
        """
        return self.bondOrder

    def getID(self):
        """
        Get Bond ID
        """
        return self.ID;


    # ----------------------------------------
    # API interface methods.
    # ========================================

    def agg_getID(self):
        """
        Get the identifier for the arc.

        NOTE:: No claims of type are made by this method
          nor any guarantee of global uniqueness.  The
          ID should be unique within the graph, however.
        """
        return self.getID();


    def agg_getNodes(self):
        """
        Get the start and end nodes.
        """
        return self.getAtoms();


    def agg_getStartNode(self):
        """
        Get the start node for this arc.
        """
        return self.getAtom_ID1


    def agg_getEndNode(self):
        """
        Get the end node for this arc.
        """
        return self.getAtom_ID2();

    def agg_getType(self):
        """
        Get the type of this arc as per the ontology
        set in the system.
        """
        return self.getOrder();


    def agg_hasField(self, FieldName, Subfield=None):
        """
        Return True if the named field/subfield is present.
        """
        raise APIError, "Unimplemented Stub."


    def agg_getField(self, FieldName, Subfield=None):
        """
        Interface method for retreival of the field
        items if they are present.
        """
        raise APIError, "Unimplemented Stub."


    def agg_listFields(self):
        """
        Interface method to list known fields.
        """
        raise APIError, "Unimplemented Stub."


    def agg_listSubfields(self, FieldName):
        """
        Interface method to list subfields of named field.
        """
        raise APIError, "Unimplemented Stub."



