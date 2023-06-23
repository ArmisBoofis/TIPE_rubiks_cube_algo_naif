
class Permutation:
    """Classe permettant de manipuler des permutations, avec opérations usuelles"""

    def __init__(self, val: list[int]):
        # Attributs calculés de la permutation : le booléen indique si le calcul a déjà été fait
        self._inverse = [False, []]
        self._produit_cycles = [False, []]
        self._produit_transpositions = [False, []]
        self._signature = [False, 1]

        # On utilise ici le mutateur défini plus bas
        Permutation.images.fset(self, val)
    
    @property
    def n(self):
        """Méthode qui renvoie la taille de l'espace de départ."""

        return len(self._images) - 1
    
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
        self._produit_transpositions[0] = False
        self._signature = [False, 1]

    @property
    def inverse(self):
        """Renvoie l'inverse de la permutation"""

        if not self._inverse[0]:
            images_inverse = [0] * (self.n)

            for k in range(1, self.n + 1):
                images_inverse[self._images[k] - 1] = k
            
            self._inverse[1] = Permutation(images_inverse)
            self._inverse[0] = True

        return self._inverse[1]
    
    @property
    def produit_cycles(self):
        """Accesseur qui renvoie la liste des cycles figurant dans le produit
        de cycles à supports disjoints associé à la permutation"""

        if not self._produit_cycles[0]:
            deja_vu = [False] * (self.n + 1)
            cycles = []

            for k in range(1, (self.n + 1)):
                y = self._images[k]

                if not deja_vu[y] and y != k:
                    cycle = [y]
                    deja_vu[y] = True

                    while self._images[y] != self._images[k]:
                        cycle.append(self._images[y])
                        y = self._images[y]
                        deja_vu[y] = True

                    cycles.append(Cycle(tuple(cycle), self.n))
            
            self._produit_cycles[1] = cycles
            self._produit_cycles[0] = True
        
        return self._produit_cycles[1]

    @property
    def produit_transpositions(self):
        """Méthode qui renvoie une décomposition en produit de transpositions
        de la permutation, sous forme de liste de cycles"""

        # On décompose chaque cycle du produit de cycles pour obtenir une décomposition complète
        if not self._produit_transpositions[0]:
            self._produit_transpositions[1] = []

            for c in self.produit_cycles:
                self._produit_transpositions[1] += c.produit_transpositions
            
            self._produit_transpositions[0] = True

        return self._produit_transpositions[1]

    @property
    def signature(self):
        """Méthode qui calcule la signature de la permutation."""

        if not self._signature[0]:
            self._signature[1] = 1 # On réinitialise la signature !

            # On multiplie les signatures des cycles apparaissant dans la décomposition en produit de cycles
            for c in self.produit_cycles:
                self._signature[1] *= c.signature

            self._signature[0] = True

        return self._signature[1]

    def __mul__(self, autre):
        """Surcharge de l'opération de composition pour les permutations"""

        if isinstance(autre, Permutation):
            if len(autre._images) != (self.n + 1):
                raise ValueError("Multiplication de deux permutations sur des ensembles différents.")
            
            nouvelles_images = [0] * self.n

            for k in range(1, (self.n + 1)):
                nouvelles_images[k - 1] = autre._images[self._images[k]]

            return Permutation(nouvelles_images)
        
        else:
            raise TypeError(f"Impossible de mutliplier une permutation avec un objet de type {type(autre)}")

    def __str__(self) -> str:
        """Méthode pour afficher une permutation"""

        ch = '|'

        for k in range(1, self.n + 1):
            ch += f' {k}'
        
        ch += ' |\n|'

        for k in range(1, self.n + 1):
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

class Cycle(Permutation):
    """Classe permettant de manipuler des permutations avec la notation de cycle"""

    def __init__(self, val: tuple[int], n: int):
        """Constructeur, qui implémente la conversion de la notation cycle à la notation usuelle"""

        # On convertit d'abord les arguments en notation usuelle
        arg_images = Cycle._cycle_vers_permutation(val, n)

        # Si les arguments sont valides, on peut les passer au constructeur parent
        if arg_images != None:
            self._representation_cycle = val # On enregistre le tuple qui représente le cycle
            super().__init__(arg_images)
        
        else:
            raise ValueError("L'argument passé ne représente pas un cycle valide.")

    @property
    def images(self):
        return super().images
    
    @images.setter
    def images(self, img: tuple[tuple[int], int]):
        """Surcharge du mutateur <images> de la classe Permutation, en prenant
        en paramètre la notation cycle."""

        try:
            val, n = img
        
        except ValueError:
            raise ValueError("L'argument passé n'est pas un tuple.")

        else:
            # On enregistre le tuple qui représente le cycle
            self._representation_cycle = val

            # On convertit les arguements en notation usuelle, puis on passe le résultat à la méthode parente
            arg_images = Cycle._cycle_vers_permutation(val, n)

            if arg_images != None:
                Permutation.images.fset(self, arg_images)
            
            else:
                raise ValueError("L'argument passé ne représente pas un cycle valide.")
    
    @property
    def representation_cycle(self):
        return self._representation_cycle
    
    @property
    def inverse(self):
        """Renvoie l'inverse du cycle, sous forme de cycle"""

        if not self._inverse[0]:
            self._inverse[1] = Cycle(self._representation_cycle[::-1], self.n)
        
        return self._inverse[1]
    
    @property
    def produit_cycles(self):
        """Décomposition en produit de cycles du cycle. On renvoie la liste
        qui contient le cycle lui-même."""

        if not self._produit_cycles[0]:
            self._produit_cycles[1] = [self]
            self._produit_cycles[0] = True
        
        return self._produit_cycles[1]

    @property
    def produit_transpositions(self):
        """Méthode qui retourne la décomposition en produit de transpositions du cycle."""
        
        if not self._produit_transpositions[0]:
            self._produit_transpositions[1] = []

            for k in range(len(self.representation_cycle) - 1):
                self._produit_transpositions[1].append(Cycle((self.representation_cycle[k], self.representation_cycle[k + 1]), self.n))

            self._produit_transpositions[0] = True

        return self._produit_transpositions[1]
    
    @property
    def signature(self):
        """Méthode qui calcule la signature du cycle."""
        return (-1) ** (len(self.representation_cycle) - 1)
    
    def __str__(self) -> str:
        """Méthode pour représenter un cycle sous forme de chaîne de caractères"""

        return f"({' '.join(map(str, self._representation_cycle))})"

    @classmethod
    def _est_valide(cls, val: tuple[int], n: int):
        """Méthode vérifiant si une liste de nombre représentant un cycle est bien valide."""

        deja_vu = [False] * (n + 1)

        for e in val:
            if e <= 0 or e > n or deja_vu[e]:
                return False

            deja_vu[e] = True

        return True

    @classmethod
    def _cycle_vers_permutation(cls, val: tuple[int], n: int):
        """Méthode permettant de convertir la notation cycle en notation usuelle."""

        if Cycle._est_valide(val, n):
                arg_images = [k for k in range(1, n + 1)] # On initialise la liste comme égale à l'identité

                # On rajoute ensuite les éléments du cycle
                for k in range(0, len(val) - 1):
                    arg_images[val[k] - 1] = val[k + 1]

                arg_images[val[-1] - 1] = val[0] # "Fermeture" du cycle

                return arg_images

        else:
            return None