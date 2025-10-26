#!/usr/bin/env python
"""Plot an example of the Nyquist representation."""
from commons import *

def main(fpath):

    f = np.logspace(5, -2, 100)
    w = 2*np.pi*f

    Rel = 10.0

    R = 100
    Zr = np.ones_like(w) * R

    C = 1e-5
    Zc = 1/(1j*C*w)

    Z = Rel +  Zr*Zc / (Zr+Zc)
    ReZ = Z.real
    ImZ = Z.imag
    modZ = np.absolute(Z)
    phase = np.angle(Z, deg=True)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel(r"f /Hz")
    ax.set_ylabel(r"$\phi$ /°")

    ax.plot(f, phase, "k.", ms=4)

    ax.set_xscale("log")
    ax.grid(True, "both", "x")

    ax.invert_yaxis()

    fmt = fpath.split(".")[-1]
    fig.savefig(fpath, dpi=DPI, format=fmt)


if __name__ == "__main__":

    try:
        fpath = sys.argv[1]
        main(fpath)        
    except IndexError as err:
        print("The argument must provide the format: png or pdf")
