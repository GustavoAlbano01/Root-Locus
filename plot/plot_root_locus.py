import matplotlib.pyplot as plt
import control as ctrl
import numpy as np
from utils.transfer_function import get_open_loop_tf

def plot_root_locus(name, num, den):
    tf = get_open_loop_tf(num, den)

    K = np.logspace(-3, 4, 5000)

    plt.figure()
    ctrl.root_locus_plot(tf, gains=K, grid=True)
    plt.title(name)