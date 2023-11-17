# mutation_operators.py

import random

def change_coefficients(poly):
    mutated_coefficients = [random.randint(-10, 10) for _ in range(len(poly.coefficients))]
    poly.coefficients = mutated_coefficients
