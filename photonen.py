# import numpy as np
from numpy import pi

WAVELENGTH = 465    # in nm
POWER = .5          # in mW
ATTENUATION = .05   # in %
DEADTIME = 35       # in ns
COUNTRATE = 20      # in MHz

def photons_per_second(lambd, power, atten, countrate):
    h = 6.626070040e-34
    c = 299792458
    E = h * (c / lambd)
    print(f"Single photon energy: {E} J")
    f_ph = power / E
    print(f"Photons per second un-attenuated: {f_ph}")
    attens = 0
    while f_ph > countrate:
        attens += 1
        f_ph = f_ph*atten
    print(f"Photons per second after {attens} attenuation passes: {f_ph}")

wavelength = WAVELENGTH * 1e-9
power = POWER * 1e-3
attenuation = ATTENUATION * 1e-2
deadtime = DEADTIME * 1e-9
countrate = COUNTRATE * 1e6
print("Input parameters:\nlambda: {} nm\nPower: {} mW\nAttenuation: {} %\n".format(WAVELENGTH, POWER, ATTENUATION))
photons_per_second(wavelength, power, attenuation, countrate)