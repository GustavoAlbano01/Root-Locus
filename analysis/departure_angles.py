import numpy as np

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
                if not np.array_equal(other, p):
                    sum_angles -= np.angle(p - other, deg=True)

            angle = 180 - sum_angles
            angles[p] = angle

    return angles