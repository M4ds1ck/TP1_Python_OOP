from math import pi

class Cercle:
    def __init__(self, rayon):
        self._rayon = None
        self.rayon = rayon

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, valeur):
        if valeur <= 0:
            raise ValueError("Rayon invalide")
        self._rayon = valeur

    @property
    def perimetre(self):
        return 2 * pi * self._rayon

    @property
    def surface(self):
        return pi * self._rayon ** 2

    def agrandir(self, pourcentage: float):
        self.rayon = self._rayon * (1 + pourcentage / 100)
