# apply_mutations.py

from polynomial import Polynomial
from mutation_operators import change_coefficients

poly1_mutant = Polynomial([3, 0, 2])
change_coefficients(poly1_mutant)
