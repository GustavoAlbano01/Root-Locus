import matplotlib.pyplot as plt
import control as ctrl
from utils.transfer_function import get_open_loop_tf

def plot_root_locus(name, num, den):
    tf = get_open_loop_tf(num, den)

    plt.figure()
    ctrl.root_locus(tf, grid=True)
    plt.title(name)