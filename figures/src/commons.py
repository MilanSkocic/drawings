#!/usr/bin/env python
"""Common libraries used for generating the figures with Python."""

# For all
import pathlib, sys, os

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, LogLocator

mpl.style.use('base')

import numpy as np
import pandas as pd

FORMATS = ["png", "pdf"]
DPI = 300

# EIS
def formatter_pi(x, pos):
    """Format axis with respect to n pi/2.""" 
    x = x * 2 * 2 # x is number of periods which correspond to 2pi and we want subidivision in pi/2 so multiply again by 2
    
    q = x // 2
    r = x % 2 
    
    if x  == 0:
        return "0"
    
    if r > 0:
        if x <= 1:
            return r"$\frac{\pi}{2}$"
        else:
            return r"{0:.0f}".format(x) + r"$\frac{\pi}{2}$"
    else:
        return r"{0:.0f}".format(q) + r"$\pi$"

def Z_R(w, R):
    r"""
    Compute complex impedance of a resistor.
    
    Parameters
    -----------
    w: array-like, shape=(n,)
        Angular frequencies in s-1.
    R: float
        Resistance in Ohms.
    
    Returns
    -----------
    Z: array-like, shape=(n,)
        Complex impedance in Ohms.
    """
    return np.ones_like(w) * R

def Z_C(w, C):
    r"""
    Compute complex impedance of a capacitor.
    
    Parameters
    -----------
    w: array-like, shape=(n,)
        Angular frequencies in s-1.
    C: float
        Capacitance in F.
    
    Returns
    -----------
    Z: array-like, shape=(n,)
        Complex impedance in Ohms.
    """
    return 1/(1j*C*w)

def Z_L(w, L):
    r"""
    Compute complex impedance of a inductor.
    
    Parameters
    -----------
    w: array-like, shape=(n,)
        Angular frequencies in s-1.
    L: float
        Inductance in H.
    
    Returns
    -----------
    Z: array-like, shape=(n,)
        Complex impedance in Ohms.
    """
    return 1j*L*w

def Z_Q(w, Q, a):
    r"""
    Compute complex impedance of a Constant Phase Element.
    
    Parameters
    -----------
    w: array-like, shape=(n,)
        Angular frequencies in s-1.
    Q: float
        CPE amplitude in S.s^a.
    
    Returns
    -----------
    Z: array-like, shape=(n,)
        Complex impedance in Ohms.
    """
    return 1/(Q*(1j*w)**a)

def Z_W(w, sigma):
    r"""
    Compute complex impedance of a semi-infinite warburg.
    
    Parameters
    -----------
    w: array-like, shape=(n,)
        Angular frequencies in s-1.
    sigma: float
        Warburg angular resistance in Omhs.s^-1/2.
    
    Returns
    -----------
    Z: array-like, shape=(n,)
        Complex impedance in Ohms.
    """
    return sigma * (1-1j) / np.sqrt(w)
    
def Z_Wd(w, Rd, nd, Td):
    r"""
    Compute complex impedance of a finite-length warburg.
    
    Parameters
    -----------
    w: array-like, shape=(n,)
        Angular frequencies in s-1.
    Rd: float
        Warburg resistance resistance in Omhs.
    nd: float
        Warburg exponent. Usually 0.5.
    Td: float
        Warburg time constant in seconds.
    
    Returns
    -----------
    Z: array-like, shape=(n,)
        Complex impedance in Ohms.
    """
    return Rd * np.tanh((1j*Td*w)**nd) / (1j*Td*w)**nd
    
def Z_Wm(w, Rm, nm, Tm):
    r"""
    Compute complex impedance of a finite-space warburg.
    
    Parameters
    -----------
    w: array-like, shape=(n,)
        Angular frequencies in s-1.
    Rm: float
        Warburg resistance resistance in Omhs.
    nm: float
        Warburg exponent. Usually 0.5.
    Tm: float
        Warburg time constant in seconds.
    
    Returns
    -----------
    Z: array-like, shape=(n,)
        Complex impedance in Ohms.
    """
    return Rm * (1/np.tanh((1j*Tm*w)**nm)) / (1j*Tm*w)**nm
