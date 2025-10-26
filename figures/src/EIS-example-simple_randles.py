#!/usr/bin/env python
"""Plot cosine and sine waves."""
from commons import *

def main(fpath):

    f = np.logspace(5, -2, 91)
    w = 2*np.pi*f

    Rel = 20.0

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

    ax.text(s=r"High $\omega$", x=0+Rel, y=-55, va="top", ha="left", backgroundcolor="w", color="C1", fontsize="small")
    ax.text(s=r"Low $\omega$", x=100+Rel, y=-55, va="top", ha="right", backgroundcolor="w", color="C1", fontsize="small")
    ax.annotate(text="", xy=(20+Rel, -45), xytext=(80+Rel, -45), 
                arrowprops=dict(arrowstyle="<->", connectionstyle="arc3, rad=0.3", color="C1"))

    ax.annotate(text="", xy=(0, 0), xytext=(Rel, 0), arrowprops=dict(arrowstyle="<->", color="C0"))
    ax.text(s="$R_{el}$", x=Rel/2, y=-5, va="center", ha="center", backgroundcolor="w", color="C0", fontsize="small")

    ax.annotate(text="", xy=(Rel, 0), xytext=(Rel+R, 0), arrowprops=dict(arrowstyle="<->", color="C0"))
    ax.text(s="$R_{ct}$", x=Rel+R/2, y=-5, va="center", ha="center", backgroundcolor="w", color="C0", fontsize="small")

    ax.annotate(text=r"$\omega _{min}$ = $\frac{1}{R_{ct}C_{dl}}$", 
                xy=(Rel+R/2, -50), color="C1",
                xytext=(Rel+R/2, -30), va="center", ha="center",
                arrowprops=dict(arrowstyle="->", color="C1"))


    ax.set_xlim(0,)
    ax.set_ylim(-60, 5)

    ax.invert_yaxis()

    fmt = fpath.split(".")[-1]
    fig.savefig(fpath, dpi=DPI, format=fmt)

if __name__ == "__main__":

    try:
        fpath = sys.argv[1]
        main(fpath)        
    except IndexError as err:
        print("The argument must provide the format: png or pdf")
