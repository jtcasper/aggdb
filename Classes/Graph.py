"""
Implementation of the AGG graph class for chemical compound graphs.
"""

import AGG
from Classes.Bond import Bond
from Classes.Node import Node

class Compound(AGG.Classes.API.Graph):

    def __init__(self, compound):
        """
        Construct a compound, which is a graph structure in AGG.
        :param id: cid of this compound
        :param atoms: dictionary of atoms as Nodes
        :param bonds: dictionary of bonds as Bonds
        """
        self.atoms = {}
        self.bonds = {}
        self.id = compound.cid
        self.addAtoms(compound)
        self.addBonds(compound)

    #----------------------
    #  Add graph elements
    #----------------------

    def addAtom(self, atom):
        """
        Add a new atom node to this graph
        :param atom: atom to be added
        :return: nothing
        """
        self.atoms.update(atom.toDict())

    def addAtoms(self, compound):
        """
        Take list of atoms in cid compound and add them to this compound
        :param compound: CID compound object
        :return: nothing
        """
        for a in compound.atoms:
            n = Node(a.aid, a.element, a.x, a.y)
            self.addAtom(n)

    def addBond(self, bond):
        """
        Add a new bond to this compound
        :param bond: bond to be added
        :return: nothing
        """

        self.bonds.update(bond.toDict())

    def addBonds(self, compound):
        """
        Take list of bonds in cid compound and add them to this compound
        :param compound: CID compound object
        :return: nothing
        """

        for arc in compound.bonds:
            b = Bond(arc.aid1, arc.aid2, arc.order)
            for val, atom in self.getNodes().items():
                if atom.getID() in b.getNodes():
                    atom.addBond(b)
            self.addBond(b)

    #----------------------
    # Define accessors
    #----------------------

    def getArcs(self):
        """
        Return bond dictionary of this compound
        :return: Bond dictionary of this compound
        """
        return self.bonds

    def getNodes(self):
        """
        Return atom dictionary of this compound
        :return: Atom dictionary of this compound
        """
        return self.atoms

    def getID(self):
        """
        Return cid of this compound
        :return: cid of compound
        """
        return self.id

    #----------------------
    # Implement API Methods
    #----------------------

    def agg_getID(self):
        """
        Get an identifier for this compound, may be None.
        :return:
        """
        return self.getID()

    def agg_getArcs(self):
        """
        Get the bonds that make up this compound.
        :return:
        """
        return self.getArcs()

    def agg_getNodes(self):
        """
        Get the atoms that make up this compound.
        :return:
        """
        return self.getNodes()

    def agg_getField(self, FieldName, Subfield=None):
        """
        Interface method for retreival of the field
        items from the graph if they are present.
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
