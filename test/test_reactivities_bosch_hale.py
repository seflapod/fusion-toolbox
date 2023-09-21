import numpy.testing as npt
import pytest

## Testing DTn fusion reaction
## Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611
@pytest.mark.parametrize(
    "test, expected, precision",
    [
        (1.0, 6.857e-21, 21),
        (2.0, 2.977e-19, 19),
        (5.0, 1.366e-17, 18),
        (10.0, 1.136e-16, 17),
        (20.0, 4.330e-16, 16),
    ])
def test_DTn_reactivity(test, expected, precision):
    """Test of the DTn fusion reactivity
    Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611

    Parameters
    ---------
    test : float
        Input ion temperature for the test
    expected : float
        Expected answer from table VIII in Bosch-Hale '92
    precision : int 
        Precision for the comparision between the Bosch-Hale parameterized value
        and the tabulated value
    """
    import fusion_toolbox.reaction_rate.bosch_hale as bh
    DTn_r= bh.BoschHaleReactivity("DTn")
    npt.assert_almost_equal(DTn_r.get_reactivity(test), expected, decimal=precision) 

## Testing DDn fusion reaction
## Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611
@pytest.mark.parametrize(
    "test, expected, precision",
    [
        (1.0, 9.933e-23, 24),
        (2.0, 3.110e-21, 22),
        (5.0, 9.128e-20, 21),
        (10.0, 6.023e-19, 20),
        (20.0, 2.603e-18, 19),
    ])
def test_DDn_reactivity(test, expected, precision):
    """Test of the DDn fusion reactivity
    Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611

    Parameters
    ---------
    test : float
        Input ion temperature for the test
    expected : float
        Expected answer from table VIII in Bosch-Hale '92
    precision : int 
        Precision for the comparision between the Bosch-Hale parameterized value
        and the tabulated value
    """
    import fusion_toolbox.reaction_rate.bosch_hale as bh
    DDn_r= bh.BoschHaleReactivity("DDn")
    npt.assert_almost_equal(DDn_r.get_reactivity(test), expected, decimal=precision) 

## Testing DDp fusion reaction
## Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611
@pytest.mark.parametrize(
    "test, expected, precision",
    [
        (1.0, 1.017e-22, 23),
        (2.0, 3.150e-21, 22),
        (5.0, 9.024e-20, 21),
        (10.0, 5.781e-19, 20),
        (20.0, 2.399e-18, 20),
    ])
def test_DDp_reactivity(test, expected, precision):
    """Test of the DDp fusion reactivity
    Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611

    Parameters
    ---------
    test : float
        Input ion temperature for the test
    expected : float
        Expected answer from table VIII in Bosch-Hale '92
    precision : int 
        Precision for the comparision between the Bosch-Hale parameterized value
        and the tabulated value
    """
    import fusion_toolbox.reaction_rate.bosch_hale as bh
    DDp_r= bh.BoschHaleReactivity("DDp")
    npt.assert_almost_equal(DDp_r.get_reactivity(test), expected, decimal=precision) 

## Testing D3Hep fusion reaction
## Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611
@pytest.mark.parametrize(
    "test, expected, precision",
    [
        (1.0, 3.057e-26, 27),
        (2.0, 1.399e-23, 24),
        (5.0, 6.377e-21, 22),
        (10.0, 2.126e-19, 20),
        (20.0, 3.482e-18, 22),
    ])
def test_D3Hep_reactivity(test, expected, precision):
    """Test of the D3Hep fusion reactivity
    Tested according to table VIII in H.-S. Bosch and G.M. Hale 1992 Nucl. Fusion 32 611

    Parameters
    ---------
    test : float
        Input ion temperature for the test
    expected : float
        Expected answer from table VIII in Bosch-Hale '92
    precision : int 
        Precision for the comparision between the Bosch-Hale parameterized value
        and the tabulated value
    """
    import fusion_toolbox.reaction_rate.bosch_hale as bh
    D3Hep_r= bh.BoschHaleReactivity("D3Hep")
    npt.assert_almost_equal(D3Hep_r.get_reactivity(test), expected, decimal=precision) 
