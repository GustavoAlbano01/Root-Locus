import numpy as np

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