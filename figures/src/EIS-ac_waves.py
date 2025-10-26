#!/usr/bin/env python
"""Plot cosine and sine waves."""
from commons import *

def main(fpath):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel(r"$\omega \cdot dt$")
    ax.set_ylabel('V /V and I /A')

    f = 1.0
    T = 1 / f
    n = np.linspace(0, 2, 1000)
    x = n * T
    phi = -np.pi/2

    w = 2*np.pi*f
    V = np.cos(w*x)
    I = 1.2*np.cos(w*x + phi)

    ax.plot(n, V, 'r-', label=r"$V_0 e^{j\omega t}$")
    ax.plot(n, I, 'b-', label=r"$I_0 e^{j(\omega t+\Phi)}$")


    ax.axvline(x=1, color='k', ls='--', marker='')
    ax.axvline(x=1 + 1/4, color='k', ls='--', marker='')
    ax.text(x=1, y= -0.75, s=r'$\Phi _{shift}$')
    ax.annotate(text="", xy=(1, -0.5), xytext=(1.25, -0.5),
               arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))


    ax.xaxis.set_major_formatter(formatter_pi)

    ax.legend(loc='lower left')
    
    fmt = fpath.split(".")[-1]
    fig.savefig(fpath, dpi=DPI, format=fmt)

if __name__ == "__main__":

    try:
        fpath = sys.argv[1]
        main(fpath)        
    except IndexError as err:
        print("The argument must provide the format: png or pdf")
