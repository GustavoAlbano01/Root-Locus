import matplotlib.pyplot as plt
from systems import SYSTEMS

from analysis.break_points import break_points
from analysis.real_axis import real_axis_segments
from analysis.jw_crossing import jw_crossing
from analysis.departure_angles import departure_angles
from plot.plot_root_locus import plot_root_locus

def analyze_system(name, num, den):

    print("Break points:", break_points(num, den))
    print("Real-axis segments:", real_axis_segments(num, den))
    print("jw crossing:", jw_crossing(num, den))
    print("Departure angles:", departure_angles(num, den))

    plot_root_locus(name, num, den)

for name, sys in SYSTEMS.items():
    analyze_system(name, sys["num"], sys["den"])

plt.show()