import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import control as ctrl

s = sp.symbols('s')

def poly_from_coeffs(coeffs):
    """Cria polinômio simbólico a partir de coeficientes"""
    return sum(c*s**(len(coeffs)-i-1) for i,c in enumerate(coeffs))

def get_open_loop_tf(num, den):
    return ctrl.TransferFunction(num, den)

def break_points(num, den):
    N = poly_from_coeffs(num)
    D = poly_from_coeffs(den)
    K = -D/N
    dK = sp.diff(K, s)
    roots = sp.solve(sp.simplify(dK), s)
    real_roots = [r.evalf() for r in roots if r.is_real]
    return real_roots

def real_axis_segments(num, den):
    poles = np.roots(den)
    zeros = np.roots(num)
    points = np.sort(np.concatenate([poles, zeros]).real)
    
    segments = []
    test_points = (points[:-1] + points[1:]) / 2
    
    for tp in test_points:
        count = sum(p.real > tp for p in poles) + sum(z.real > tp for z in zeros)
        if count % 2 == 1:
            segments.append(tp)
    return segments

def jw_crossing(num, den):
    K = sp.symbols('K', real=True)
    N = poly_from_coeffs(num)
    D = poly_from_coeffs(den)
    char_eq = D + K*N
    poly = sp.Poly(char_eq, s)
    
    w = sp.symbols('w', real=True)
    jw_eq = sp.simplify(char_eq.subs(s, sp.I*w))
    real_part = sp.re(jw_eq)
    imag_part = sp.im(jw_eq)
    
    sol = sp.solve([real_part, imag_part],[w,K])
    return sol

def departure_angles(num, den):
    poles = np.roots(den)
    zeros = np.roots(num)
    angles = {}
    
    for p in poles:
        if np.imag(p) != 0:
            sum_angles = 0
            for z in zeros:
                sum_angles += np.angle(p - z, deg=True)
            for other in poles:
                if other != p:
                    sum_angles -= np.angle(p - other, deg=True)
            angle = 180 - sum_angles
            angles[p] = angle
    return angles

def analyze_system(name, num, den):
    tf = get_open_loop_tf(num, den)
    
    plt.figure()
    ctrl.root_locus(tf, grid=True)
    plt.title(name)

SYSTEMS = {
    "Sistema 1": {
        "num": [1, -2, 2],
        "den": [1, 3, 2]
    },
    "Sistema 2": {
        "num": [1, -6, 8],
        "den": [1, 6, 25]
    },
    "Sistema 3": {
        "num": [1, 5],
        "den": [1, 4, 6, 4]
    }
}

for name, sys in SYSTEMS.items():
    analyze_system(name, sys["num"], sys["den"])

plt.show()