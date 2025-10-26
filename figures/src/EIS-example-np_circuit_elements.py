#!/usr/bin/env python
"""Plot cosine and sine waves."""
from commons import *

def main(fpath):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")

    ax.set_xlabel(r"ReZ /$\Omega$")
    ax.set_ylabel(r"ImZ /$\Omega$")

    f = np.logspace(5, -2, 100)
    w = np.pi*f*2

    color = "k"
    z = Z_R(w, R=100.0)
    x = z.real
    y = z.imag
    ax.plot(x, y, color=color, marker="s", ms=6, label="Resistor")


    color = "C0"
    z = Z_C(w, C=1e-2)
    x = z.real
    y = z.imag
    ax.plot(x, y, color=color, marker=".", ms=4, label="Capacitor")

    color = "C1"
    z = Z_L(w, L=1e-2)
    x = z.real
    y = z.imag
    ax.plot(x, y, color=color, marker=".", ms=4, label="Inductor")


    color = "C2"
    z = Z_Q(w, Q=1e-2, a=0.9)
    x = z.real
    y = z.imag
    ax.plot(x, y, color=color, marker=".", ms=4, label="CPE")


    color = "C4"
    z = Z_W(w, sigma=100.0)
    x = z.real
    y = z.imag
    ax.plot(x, y, color=color, marker="s", ms=4, label="Warburg")

    color = "C5"
    z = Z_Wd(w, Rd=500.0, nd=0.5, Td=1.0)
    x = z.real
    y = z.imag
    ax.plot(x, y, color=color, marker="d", ms=4, label="FLW")

    color = "C6"
    z = Z_Wm(w, Rm=500.0, nm=0.5, Tm=1.0)
    x = z.real
    y = z.imag
    ax.plot(x, y, color=color, marker=".", ms=4, label="FSW")


    ax.set_xlim(-50, 600)
    ax.set_ylim(-500, 50)

    ax.invert_yaxis()

    ax.legend(ncol=1)

    fmt = fpath.split(".")[-1]
    fig.savefig(fpath, dpi=DPI, format=fmt)

if __name__ == "__main__":

    try:
        fpath = sys.argv[1]
        main(fpath)        
    except IndexError as err:
        print("The argument must provide the format: png or pdf")
