import numpy as np
from impedanciaAbsorbente import ImpedanciaAbsorbente
import matplotlib.pyplot as plt

''' 

Armar estudios:

Info: https://www.jochenschulz.me/en/blog/rockwool-glasswool-hemp-best-absorber-material
## Estudio 1) Efecto de la Resistividad al paso del aire, dejando otras variables igual

## Estudio 2) Efecto del espesor

## Estudio 3) Efecto de la porosidad

'''

mat1 = ImpedanciaAbsorbente(resAire=5800, freqUnica= False, bins=500)
mat1_zs = mat1.zs
mat1_R = np.round(abs(mat1.R),2)
mat1_alpha = np.round(abs(mat1.alpha),2)

mat2 = ImpedanciaAbsorbente(resAire=15000, freqUnica= False, bins=500)
mat2_zs = mat2.zs
mat2_R = np.round(abs(mat2.R),2)
mat2_alpha = np.round(abs(mat2.alpha),2)

mat3 = ImpedanciaAbsorbente(resAire=25000, freqUnica= False, bins=500)
mat3_zs = mat3.zs
mat3_R = np.round(abs(mat3.R),2)
mat3_alpha = np.round(abs(mat3.alpha),2)

freq = mat1.freq

plt.plot(freq,mat1_alpha,freq,mat2_alpha,freq,mat3_alpha)
plt.show()

plt.plot(freq,mat1_R,freq,mat2_R,freq,mat3_R)
plt.show()