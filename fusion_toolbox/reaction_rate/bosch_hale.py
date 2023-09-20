import numpy as np
import sys
import matplotlib.pyplot as plt

## Class for Bosch-Hale reactivity
## All of it comes from: H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611
class Reactivity:

	known_reactions = ["DDn", "DDp", "DTn", "D3Hep"]

	# The space is here so the indexing matches the paper
	DDn_Cs   = [" ", 5.43360e-12, 5.85778e-3, 7.68222e-3, 0.0, -2.96400e-6, 0.0, 0.0]
	DDp_Cs   = [" ", 5.65718e-12, 3.41267e-3, 1.99167e-3, 0.0, 1.05060e-5, 0.0, 0.0]
	DTn_Cs   = [" ", 1.1302e-9, 1.51361e-2, 7.51886e-2, 4.60643e-3, 1.35e-2, -1.0675e-4, 1.366e-5]
	D3Hep_Cs = [" ", 5.51036e-10, 6.41918e-3, -2.02896e-3, -1.91080e-5, 1.35776e-4, 0.0, 0.0 ]

	DDn_Bg   = 31.3970
	DDp_Bg   = 31.3970
	DTn_Bg   = 34.3827
	D3Hep_Bg = 68.7508

	DDn_mr   = 937814
	DDp_mr   = 937814
	DTn_mr   = 1124656
	D3Hep_mr = 1124572

	Cs_dict = {"DDn" : DDn_Cs, "DDp" : DDp_Cs, "DTn" : DTn_Cs, "D3Hep" : D3Hep_Cs}

	Bg_dict = {"DDn" : DDn_Bg, "DDp" : DDp_Bg, "DTn" : DTn_Bg, "D3Hep" : D3Hep_Bg}
	mr_dict = {"DDn" : DDn_mr, "DDp" : DDn_mr, "DTn" : DTn_mr, "D3Hep" : D3Hep_mr}

	def __init__(self, reaction):

		if reaction in self.known_reactions:
			self.reaction = reaction
		else:
            # THIS IS HORRIBLE PLZ FIX LATER!!!
			print("Unknown reaction error.")
			sys.exit()

		self.C  = self.Cs_dict[self.reaction]
		self.Bg = self.Bg_dict[self.reaction]
		self.mr = self.mr_dict[self.reaction]

	def get_reactivity(self, Temp):

		fraction_top    = Temp*(self.C[2] + Temp*(self.C[4] + Temp*self.C[6]))
		fraction_bottom = 1 + Temp*(self.C[3] + Temp*(self.C[5] + Temp*self.C[7]))

		theta = Temp/(1 - fraction_top/fraction_bottom)
		xi    = (self.Bg**2/(4*theta))**(1/3)

		sigmaV = self.C[1]*theta*np.sqrt(xi/(self.mr*Temp**3))*np.exp(-3*xi)

		return sigmaV

	def plot_reactivity(self):

		T_i = np.logspace(-1, 2, 1000)

		fig, ax = plt.subplots(1,1)

		ax.loglog(T_i, [self.get_reactivity(Temp) for Temp in T_i])
		ax.set_title(f"Reactivity plot of {self.reaction}")
		ax.set_ylabel(r"Reactivity (cm$^3$/s)")
		ax.set_xlabel("Ion Temperature (keV)")

		plt.show()

