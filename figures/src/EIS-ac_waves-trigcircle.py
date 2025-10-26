#!/usr/bin/env python
"""Plot cosine and sine waves in trigonometric circle."""
from commons import *

def main(fpath):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.grid(False)
    #ax.set_axis_off()

    ax.spines["left"].set_position('center')
    ax.spines["left"].set_color("C7")

    ax.spines["right"].set_color('none')

    ax.spines["bottom"].set_position('center')
    ax.spines["bottom"].set_color("k")

    ax.spines["top"].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))

    ax.set_xlabel("Real Part", loc="right", color='k', fontsize="x-small")
    ax.set_ylabel("Imag. Part", loc="top", color="C7", fontsize="x-small")

    # trigonometric circle and center and positions of +/- pi/4
    r = 1.0
    phase = np.linspace(0, 2*np.pi, 100)
    circle = r*np.exp(1j*phase)
    x = circle.real
    y = circle.imag
    ax.plot(x, y, "k-", lw=1)


    dr = 0.05
    rs = np.linspace(r*(1-dr), r*(1+dr), 10)
    angles = (0, np.pi/2, np.pi, 3*np.pi/2)
    labels = ("", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$")
    d = 0.1
    dxdys = ((0,0), (d, 0), (0, d), (d,0))
    for angle, label, dxdy in zip(angles, labels, dxdys):
        
        # ticks in circle
        z = rs * np.exp(1j*angle)
        x, y = z.real, z.imag
        ax.plot(x, y, "k-")
        
        # text over ticks
        z = r*(1+dr*4) * np.exp(1j*angle)
        x, y = z.real, z.imag
        dx, dy = dxdy
        ax.text(s=label, x=x+dx, y=y+dy, va="center", ha="center", color="C2")

    # plot voltage and current and annotate their vectors
    V0 = 1.9
    phi_V = np.pi/3
    V = V0*np.exp(1j*phi_V)
    x = V.real / V0
    y = V.imag / V0
    arrowprops = dict(arrowstyle="->", shrinkA=0, shrinkB=0, color="r")
    ax.annotate(text="", xy=(x, y), xytext=(0,0), arrowprops=arrowprops)
    ax.text(s=r"$V(\omega)/V_0 \cdot e^{j\omega \cdot t}$", x=x*1.1, y=y*1.1, fontsize="x-small", color="r")

    I0 = 0.7
    phi_I = np.pi/20
    I = I0*np.exp(1j*phi_I)
    x = I.real / I0
    y = I.imag / I0
    arrowprops = dict(arrowstyle="->", shrinkA=0, shrinkB=0, color="b")
    ax.annotate(text="", xy=(x, y), xytext=(0,0), arrowprops=arrowprops)
    ax.text(s=r"$I(\omega)/I_0 \cdot e^{j(\omega \cdot t - \phi)}$", x=x*1.1, y=y*1.1, fontsize="x-small", color="b")


    # annotate phase shift
    arrowprops = dict(arrowstyle="->", shrinkA=0, shrinkB=0, color="C2", connectionstyle="arc3, rad=-0.1")
    xy = np.real(I/I0)/2, np.imag(I/I0)/2
    xytext = np.real(V/V0)/2, np.imag(V/V0)/2
    ax.annotate(text="", xytext=xytext, xy=xy, arrowprops=arrowprops)
    z = np.exp(1j*(phi_V+phi_I)/2) / 1.9
    x, y = z.real, z.imag
    ax.text(s=r"$\Phi$", x=x, y=y, va="center", ha="left", color="C2")

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    fmt = fpath.split(".")[-1]
    fig.savefig(fpath, dpi=DPI, format=fmt)


if __name__ == "__main__":

    try:
        fpath = sys.argv[1]
        main(fpath)        
    except IndexError as err:
        print("The argument must provide the format: png or pdf")
