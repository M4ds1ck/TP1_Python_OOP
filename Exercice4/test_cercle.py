from cercle import Cercle
from math import pi

c = Cercle(3)
print(c.perimetre)
print(c.surface)

try:
    c.rayon = -5
except ValueError as e:
    print("Erreur capturee :", e)
