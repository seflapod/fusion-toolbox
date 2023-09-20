import fusion_toolbox.reaction_rate.bosch_hale as bh
import numpy.testing as npt

def test_DTn_reactivity():
    DTn_r= bh.Reactivity("DDp")
    test_result= 1.3e-17 ## from NRL plasma formulary 
    test_input = 5.0 # keV
    npt.assert_almost_equal(DTn_r.get_reactivity(test_input), test_result, decimal=2) 
