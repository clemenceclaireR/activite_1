#!/usr/bin/python

from math import *

a = input("Veuillez entrer le cote a :")
b = input("Veuillez entrer le cote b :")
c = input("Veuillez entrer le cote c :")

cote_a = (float(a))
cote_b = (float(b))
cote_c = (float(c))

demi_perimetre = (cote_a + cote_b + cote_c) / 2 
aire = sqrt(demi_perimetre*(demi_perimetre-cote_a)*(demi_perimetre-cote_b*(demi_perimetre-cote_c)))

print("Longueur des cotes =", cote_a, cote_b, cote_c)
print("Perimetre =", 2*demi_perimetre, "Aire =", aire)
