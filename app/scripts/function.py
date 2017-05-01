from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob


def damped_vibrations(t, A, b, w):
    return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution+1)
    u = damped_vibrations(t, A, b, w)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, u)
    plt.title('A=%g, b=%g, w=%g' % (A, b, w))
    if not os.path.isdir('app/scripts/static'):
        os.mkdir('app/scripts/static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('app/scripts/static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join('app/scripts/static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile
