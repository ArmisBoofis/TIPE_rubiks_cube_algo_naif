
class Permutation:
    def __init__(self, val: list[int]):
        self._inverse = [False, []]
        self._produit_cycles = [False, []]
        self.images = val # On utilise ici le mutateur défini plus bas
    
    @property
    def images(self):
        """Accesseur de la propriété <images>"""
        return self._images[1:]
    
    @images.setter
    def images(self, val: list[int]):
        """Mutateur de la propriété <images>"""

        val.insert(0, 0) # Permet d'éviter les problèmes d'indice, puisqu'on compte à partir de 1

        if not Permutation._est_valide(val):
            raise ValueError("La liste donnée ne définit pas une permutation valide")
        
        # On modifie la valeur des images et on marque toutes les autres propriétés calculables comme n'étant pas initialisées
        self._images = val
        self._inverse[0] = False
        self._produit_cycles[0] = False

    @property
    def inverse(self):
        """Renvoie l'inverse de la permutation"""

        if not self._inverse[0]:
            images_inverse = [0] * (len(self._images) - 1)

            for k in range(1, len(self._images)):
                images_inverse[self._images[k] - 1] = k
            
            self._inverse[1] = Permutation(images_inverse)
            self._inverse[0] = True

        return self._inverse[1]
    
    @property
    def produit_cycles(self):
        """Accesseur qui renvoie la liste des cycles figurant dans le produit
        de cycles à supports disjoints associé à la permutation"""

        if not self._produit_cycles[0]:
            deja_vu = [False] * len(self._images)
            cycles = []

            for k in range(1, len(self._images)):
                y = self._images[k]

                if not deja_vu[y] and y != k:
                    cycle = [k for k in range(len(self._images))]
                    cycle[k] = y
                    deja_vu[y] = True

                    while self._images[y] != self._images[k]:
                        cycle[y] = self._images[y]
                        y = self._images[y]
                        deja_vu[y] = True


                    cycles.append(Permutation(cycle[1:]))
            
            self._produit_cycles[1] = cycles
            self._produit_cycles[0] = True
        
        return self._produit_cycles[1]

    def __mul__(self, perm2):
        """Surcharge de l'opération de composition pour les permutations"""

        if len(perm2._images) != len(self._images):
            raise ValueError("Multiplication de deux permutations sur des ensembles différents.")
        
        nouvelles_images = [0] * (len(self._images) - 1)

        for k in range(1, len(self._images)):
            nouvelles_images[k - 1] = perm2._images[self._images[k]]

        return Permutation(nouvelles_images)

    def __str__(self) -> str:
        """Méthode pour afficher une permutation"""

        ch = '|'

        for k in range(1, len(self._images)):
            ch += f' {k}'
        
        ch += ' |\n|'

        for k in range(1, len(self._images)):
            ch += f' {self._images[k]}'
        
        ch += ' |'

        return ch

    @classmethod
    def _est_valide(cls, images):
        """Méthode de classe vérifiant si une liste d'images définit bien une permutation"""

        n = len(images) - 1
        deja_vu = [False] * (n + 1)

        for k in range(1, n + 1):
            if images[k] > n or images[k] <= 0 or deja_vu[images[k]]:
                return False
            
            deja_vu[images[k]] = True
        
        return True

# TODO :
# - décomposition en produit de transpositions
# - signature