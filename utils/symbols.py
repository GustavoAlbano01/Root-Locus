import sympy as sp

s = sp.symbols('s')

def poly_from_coeffs(coeffs):
    return sum(c*s**(len(coeffs)-i-1) for i,c in enumerate(coeffs))