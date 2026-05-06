import sympy as sp
from utils.symbols import s, poly_from_coeffs

def break_points(num, den):
    N = poly_from_coeffs(num)
    D = poly_from_coeffs(den)

    K = -D/N
    dK = sp.diff(K, s)

    roots = sp.solve(sp.simplify(dK), s)
    real_roots = [r.evalf() for r in roots if r.is_real]
    return real_roots