# test_mutants.py

from polynomial import Polynomial
from mutation_operators import change_coefficients

def test_change_coefficients():
    poly = Polynomial([3, 0, 2])
    original_coefficients = poly.coefficients.copy()

    change_coefficients(poly)
    assert poly.coefficients != original_coefficients
