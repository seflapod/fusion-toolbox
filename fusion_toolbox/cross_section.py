import numpy as np

class CrossSection:
    """
    Class to hold cross section data for a given nuclear reaction

    Parameters
    ----------
    reaction : string
        String name for the nuclear reaction

    Attributes
    ----------
    reaction : string
        String name for the nuclear reaction
    reactant1 : string
        String name for the first reactant of the nuclear reaction
    m1 : double
        Mass (atomic mass units) of reactant1
    reactant2 : string
        String name for the second reactant of the nuclear reaction
    m2 : double
        Mass (atomic mass units) of reactant2
    E_com : np array of doubles
        Center of mass energies (keV) of reactants
    xs : np array of doubles
        cross section of the reaction at each energy E_com

    """
    known_reactions = ["DDn", "DDp", "DTn", "D3Hep"]
    mD, mT, m3He = 2.014, 3.016, 3.016  # mass of each rectant in known_reactions

    def __init__(self, reaction):
        if reaction in self.known_reactions:
            self.reaction = reaction
        else:
            raise ValueError(f"Unknown reaction. Should be one of {self.known_reactions}")
        
        data = np.loadtxt(self.reaction + ".txt", comments = ["#", "//"])
        E_incident = data[:,0] # energy (MeV) of incident reactant
        xs = data[:,1] # cross section in barns
        # convert E_incident to E_com based on masses
        
    