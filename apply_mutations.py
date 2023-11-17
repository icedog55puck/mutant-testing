# apply_mutations.py

from polynomial import Polynomial
from mutation_operators import change_coefficients

poly1_mutant = Polynomial([3, 0, 2])
change_coefficients(poly1_mutant)

poly2_mutant = Polynomial([1, -1])
change_exponentiation(poly2_mutant)

poly3_mutant = Polynomial([3, 0, 2])
remove_coefficients(poly3_mutant)

poly4_mutant = Polynomial([1, -1])
add_redundant_code(poly4_mutant)
