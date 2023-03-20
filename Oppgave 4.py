# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:50:14 2023

@author: Skogs
"""
import numpy as np
from numpy import linalg as La
import matplotlib.pyplot as plt

#DEFINISJON AV FUNKSJONER
# Legger inn koeffisientmatrisa A og deretter F(x,y) (som vektorfunksjon) som Pythonfunksjon
A = np.array([[0.78,0.04,0.09,0.09],[0.10,0.85,0.04,0.01],[0.05, 0.05, 0.80, 0.10],[0.01, 0.13, 0.01, 0.85]])
A = np.transpose(A)

def F(xvektor):
    dzvektor = A@xvektor
    return dzvektor

# Initialveriene
init = np.array([[1],[0],[0],[0]])

# Parametre som ofte endres (tidsinnstillinger og initialisering):
t_start=0 # Nedre grense for området på t-aksen
t_stopp= 20; # Øvre grense for området på t-aksen
dt = 1; # Fastsetter skittlengden

# Utregnede og standariserte parametre (som kan gjenbrukes ved justeringer):
n = int((t_stopp-t_start)/dt)+1 # Antall t_verdier of funksjonsverdier som skal fylles ut

# "Tomme" radvektorer (med bare nuller) for innsetting av data
tverdier = np.zeros(n) # Tidspuktene t
averdier = np.zeros(n) # Funksjonsverdiene for x(t)
bverdier = np.zeros(n) # Funksjonsverdiene for y(t)
cverdier = np.zeros(n) # Funksjonsverdiene for z(t)
dverdier = np.zeros(n)

# Initialisering av datavektorene:
tverdier[0]=t_start #Starttidspunktet
averdier[0]=init[0] 
bverdier[0]=init[1] 
cverdier[0]=init[2] 
dverdier[0]=init[3]

xi=init
for i in range(0,n-1):
    xi=F(xi)
    tverdier[i+1]=tverdier[i]+dt
    averdier[i+1]=xi[0]
    bverdier[i+1]=xi[1]
    cverdier[i+1]=xi[2]
    dverdier[i+1]=xi[3]

# PLOTTING
plt.close('all')
plt.plot(tverdier,averdier, ".r",label="A")
plt.plot(tverdier,bverdier, ".b",label="B")
plt.plot(tverdier,cverdier, ".g",label="C")
plt.legend()
plt.grid()
plt.show()



