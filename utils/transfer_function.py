import control as ctrl

def get_open_loop_tf(num, den):
    return ctrl.TransferFunction(num, den)