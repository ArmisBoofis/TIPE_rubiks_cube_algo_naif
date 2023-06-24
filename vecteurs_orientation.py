from outils_permutations import Permutation


class VecteurOrientation():
    """Classe permettant de représenter un vecteur orientation."""

    def __init__(self, val: list[int], modulo: int):
        """Constructeur ; simple initialisation des attributs."""

        self._modulo = modulo
        self._valeurs = val

        self._reste() # On "normalise" le vecteur passé en argument
    
    @property
    def modulo(self):
        return self._modulo
    
    @modulo.setter
    def modulo(self, modulo):
        self._modulo = modulo
        self._reste()
    
    @property
    def valeurs(self):
        return self._valeurs

    @valeurs.setter
    def valeurs(self, val: list[int]):
        self._valeurs = val
        self._reste()

    def __add__(self, autre):
        """Méthode permettant d'additionner deux vecteurs orientations."""

        if isinstance(autre, VecteurOrientation):
            if len(autre.valeurs) != len(self.valeurs) or autre.modulo != self.modulo:
                raise ValueError("Impossible d'additionner deux vecteurs orientations de caractéristiques différentes (taille, modulo).")
            
            else:
                nouvelles_valeurs = []

                # On additionne d'abord les coordonnées deux à deux
                for k in range(len(self.valeurs)):
                    nouvelles_valeurs.append(self._valeurs[k] + autre.valeurs[k])
                
                # On retourne un nouveau vecteur orientation construit à partir des deux
                return VecteurOrientation(nouvelles_valeurs, self.modulo)
        
        else:
            raise TypeError(f"Impossible d'additionner un vecteur orientation avec un objet de type {type(autre)}")

    def __rmul__(self, perm):
        """Méthode permettant de faire agir une permutation sur un vecteur orientation,
        en mélangeant les éléments du vecteur orientation."""

        if isinstance(perm, Permutation):
            # Il faut vérifier que la permutation agit sur un ensemble de même taille que le vecteur
            if perm.n == len(self.valeurs):
                arg_valeurs = [0] * len(self.valeurs) # On initalise un nouveau vecteur orientation vierge

                for k in range(len(self.valeurs)):
                    arg_valeurs[k] = self.valeurs[perm.images[k] - 1]
                
                # On retourne le vecteur orientation correspondant
                return VecteurOrientation(arg_valeurs, self.modulo)

            else:
                raise ValueError("Multiplication d'un vecteur orientation par une permutation de mauvaise taille.")
        
        else:
            return NotImplemented

    def __str__(self) -> str:
        """Méthode permettant la représentation d'un vecteur orientation par une chaîne de caractères ( et
        donc l'affichage d'un tel objet)."""

        return f"({' '.join(map(str, self.valeurs))})"

    def _reste(self):
        """Méthode utilitaire qui prend le reste de tous les
        éléments du vecteur et qui renvoie le vecteur dont les éléments
        sont les restes de la division euclidienne de ces derniers par <modulo>."""

        self._valeurs = list(map(lambda x : x % self._modulo, self._valeurs))