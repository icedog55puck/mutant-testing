# mutation_operators.py

import random

def change_coefficients(poly):
    mutated_coefficients = [random.randint(-10, 10) for _ in range(len(poly.coefficients))]
    poly.coefficients = mutated_coefficients
def change_exponentiation(poly):
    for i in range(len(poly.coefficients)):
        poly.coefficients[i] = poly.coefficients[i] ** 2

def remove_coefficients(poly):
    indices_to_remove = random.sample(range(len(poly.coefficients)), random.randint(1, len(poly.coefficients)))
    for idx in indices_to_remove:
        poly.coefficients[idx] = 0
def add_redundant_code(poly):
    for i in range(len(poly.coefficients)):
        # Introduce a redundant calculation
        poly.coefficients[i] = poly.coefficients[i] * 1