import sympy as sp
from utils.symbols import s, poly_from_coeffs

def jw_crossing(num, den):
    K = sp.symbols('K', real=True)

    N = poly_from_coeffs(num)
    D = poly_from_coeffs(den)
    char_eq = D + K*N

    w = sp.symbols('w', real=True)
    jw_eq = sp.simplify(char_eq.subs(s, sp.I*w))

    real_part = sp.re(jw_eq)
    imag_part = sp.im(jw_eq)

    sol = sp.solve([real_part, imag_part],[w,K])
    return sol