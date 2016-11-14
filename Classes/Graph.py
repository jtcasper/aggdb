"""
Implementation of the AGG graph class for chemical compound graphs.
"""

import AGG

class Compound(AGG.Classes.API.Graph):

    def __init__(self, id=None, atoms=None, bonds=None):
        """
        Construct a compound, which is a graph structure in AGG.
        :param id: cid of this compound
        :param atoms: dictionary of atoms as Nodes
        :param bonds: dictionary of bonds as Bonds
        """
        self.atoms = {}
        self.bonds = {}
        if atoms is not None:
            self.atoms = atoms
        if bonds is not None:
            self.bonds = bonds
        self.id = id

    #----------------------
    #  Add graph elements
    #----------------------

    def addAtom(self, atom):
        """
        Add a new atom node to this graph
        :param atom: atom to be added
        :return: nothing
        """
        self.atoms.update(atom)

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

        self.bonds.update(bond)

    def addBonds(self, compound):
        """
        Take list of bonds in cid compound and add them to this compound
        :param compound: CID compound object
        :return: nothing
        """

        for arc in compound.bonds:
            b = Bond(arc.aid1, arc.aid2, arc.order)
            self.addBond(b)

    #----------------------
    # Define accessors
    #----------------------

    def getBonds(self):
        """
        Return bond dictionary of this compound
        :return: Bond dictionary of this compound
        """
        return self.bonds

    def getAtoms(self):
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
        return self.getBonds()

    def agg_getNodes(self):
        """
        Get the atoms that make up this compound.
        :return:
        """
        return self.getAtoms()

    def agg_getField(self, FieldName, Subfield=None):
        """
        Interface method for retreival of the field
        items from the graph if they are present.
        """
        raise APIError, "Unimplemented Stub."


    def agg_hasField(self, FieldName, Subfield=None):
        """
        Return True if the named field/subfield is present.
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
