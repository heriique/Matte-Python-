# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:22:29 2023

@author: Skogs
"""
import numpy as np
import matplotlib.pyplot as plt
#DEFINISJON AV FUNKSJONER
# Matrise i oppgave 3
A = np.array([[-2, 1, 3.4], [-1.2, 0.2, +2.4], [-0.5, 0.5, 0.7]])

def F(xvektor):
    dzvektor = A@xvektor
    return dzvektor

# Initialveriene
init = np.array([[1],[0],[0]])

# Parametre som ofte endres (tidsinnstillinger og initialisering):
t_start=0 # Nedre grense for området på t-aksen
t_stopp= 10; # Øvre grense for området på t-aksen
dt = 0.1; # Fastsetter skittlengden

# Utregnede og standariserte parametre (som kan gjenbrukes ved justeringer):
n = int((t_stopp-t_start)/dt)+1 # Antall t_verdier of funksjonsverdier som skal fylles ut

# "Tomme" radvektorer (med bare nuller) for innsetting av data
tverdier = np.zeros(n) # Tidspuktene t
xverdier = np.zeros(n) # Funksjonsverdiene for x(t)
yverdier = np.zeros(n) # Funksjonsverdiene for y(t)
zverdier = np.zeros(n) # Funksjonsverdiene for z(t)

# Initialisering av datavektorene:
tverdier[0]=t_start #Starttidspunktet
xverdier[0]=init[0] #Startverdien for x i første element
yverdier[0]=init[1] #Startverdien for y i første element
zverdier[0]=init[2] #Startverdien for z i første element

xi=init
for i in range(0,n-1):
    xi=xi+dt*F(xi)
    tverdier[i+1]=tverdier[i]+dt
    xverdier[i+1]=xi[0]
    yverdier[i+1]=xi[1]
    zverdier[i+1]=xi[2]

# PLOTTING
plt.close('all')
plt.plot(tverdier,xverdier, "-r",label="x(t)")
plt.plot(tverdier,yverdier, "-b",label="y(t)")
plt.plot(tverdier,zverdier, "-g",label="z(t)")
plt.legend()
plt.grid()
plt.show()
 