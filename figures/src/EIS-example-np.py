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
    ax.set_aspect("equal")
    ax.set_xlabel(r"ReZ /$\Omega$")
    ax.set_ylabel(r"ImZ /$\Omega$")


    ax.plot(ReZ, ImZ, "k.", ms=4)
    ax.plot(ReZ[0], ImZ[0], "C1", ms=6)
    ax.plot(ReZ[-1], ImZ[-1], "C1", ms=6)


    ax.text(s="High Frequency", x=0+Rel, y=-40, va="top", ha="left", backgroundcolor="w", color="C1", fontsize="small")
    ax.text(s="Low Frequency", x=100+Rel, y=-40, va="top", ha="right", backgroundcolor="w", color="C1", fontsize="small")
    ax.annotate(text="", xy=(35+Rel, -40), xytext=(65+Rel, -40), 
                arrowprops=dict(arrowstyle="<->", connectionstyle="arc3, rad=0.2", color="C1"))
    ax.text(s=r"$\omega$", x=50+Rel, y=-44, va="center", ha="center", backgroundcolor="w", color="C1", fontsize="small")

    ax.annotate(text=r"$\omega=\infty$", xy=(0+Rel, 0), xytext=(30+Rel, 0), va="center", ha="right", 
                arrowprops=dict(arrowstyle="->"))

    ax.annotate(text=r"$\omega=0$", xy=(100+Rel, 0), xytext=(70+Rel, 0), va="center", ha="left",
                arrowprops=dict(arrowstyle="->"))

    ax.set_xlim(0,)
    ax.set_ylim(-55, 5)

    ax.invert_yaxis()

    fmt = fpath.split(".")[-1]
    fig.savefig(fpath, dpi=DPI, format=fmt)


if __name__ == "__main__":

    try:
        fpath = sys.argv[1]
        main(fpath)        
    except IndexError as err:
        print("The argument must provide the format: png or pdf")
