from outils_permutations import Permutation
from vecteurs_orientation import VecteurOrientation


class Mouvement():
    """Classe permettant de représenter un mouvement du Rubik's Cube."""

    def __init__(self, perm_sommets: Permutation, vect_sommets: VecteurOrientation, perm_aretes: Permutation, vect_aretes: VecteurOrientation):
        """Constructeur ; prend en paramètre les quatres deux permutations et vecteurs orientations
        caractérisant un mouvement du Rubik's Cube."""

        # On vérifie d'abord le type et la bonne définition des paramètres
        if isinstance(perm_sommets, Permutation) and isinstance(perm_aretes, Permutation) and isinstance(vect_sommets, VecteurOrientation) and isinstance(vect_aretes, VecteurOrientation):
            if perm_sommets.n == 8 and perm_aretes.n == 12 and vect_sommets.n == 8 and vect_sommets.modulo == 3 and vect_aretes.n == 12 and vect_aretes.modulo == 2:
                # Si on en arrive là, tous les arguments sont corrects !
                self._perm_sommets = perm_sommets
                self._perm_aretes = perm_aretes
                self._vect_sommets = vect_sommets
                self._vect_aretes = vect_aretes

            else:
                # Les arguments n'ont pas les bonnes caractéristiques
                raise ValueError(
                    "Les permutations et vecteurs orientations donnés ne représentent pas un mouvement valide.")

        else:
            # Problème de typage
            raise TypeError("Les arguements passés n'ont pas le bon type.")

    @property
    def perm_sommets(self) -> Permutation:
        """Accesseur de la permutation sur les sommets"""
        return self._perm_sommets

    @perm_sommets.setter
    def perm_sommets(self, perm: Permutation):
        """Mutateur de la permutation sur les sommets"""
        if isinstance(perm, Permutation):
            if perm.n == 8:
                self._perm_sommets = perm

            else:
                raise ValueError(
                    "La permutation passée n'est pas de la bonne taille.")

        else:
            raise TypeError("L'argument passé n'est pas une permutation.")

    @property
    def perm_aretes(self) -> Permutation:
        """Accesseur de la permutation sur les aretes"""
        return self._perm_aretes

    @perm_aretes.setter
    def perm_aretes(self, perm):
        """Mutateur de la permutation sur les arêtes"""
        if isinstance(perm, Permutation):
            if perm.n == 12:
                self._perm_aretes = perm

            else:
                raise ValueError(
                    "La permutation passée n'est pas de la bonne taille.")

        else:
            raise TypeError("L'argument passé n'est pas une permutation.")

    @property
    def vect_sommets(self) -> VecteurOrientation:
        """Accesseur du vecteur orientation sur les sommets"""
        return self._vect_sommets

    @vect_sommets.setter
    def vect_sommets(self, vect):
        """Mutateur du vecteur orientation des sommets"""
        if isinstance(vect, VecteurOrientation):
            if vect.n == 8 and vect.modulo == 3:
                self._vect_sommets = vect

            else:
                raise ValueError(
                    "Le vecteur orientation sur les sommets passé n'est pas valide.")

        else:
            raise TypeError(
                "L'argument passé n'est pas un vecteur orientation.")

    @property
    def vect_aretes(self) -> VecteurOrientation:
        """Accesseur du vecteur orientation sur les arêtes"""
        return self._vect_aretes

    @vect_aretes.setter
    def vect_aretes(self, vect):
        """Mutateur du vecteur orientation sur les arêtes"""
        if isinstance(vect, VecteurOrientation):
            if vect.n == 12 and vect.modulo == 2:
                self._vect_aretes = vect

            else:
                raise ValueError(
                    "Le vecteur orientation sur les arêtes passé n'est pas valide.")

        else:
            raise TypeError(
                "L'argument passé n'est pas un vecteur orientation.")

    def __mul__(self, autre):
        """Méthode permettant de composer deux mouvements du Rubik's Cube."""
        if isinstance(autre, Mouvement):
            # On multiplie deux à deux les permutations sur les arêtes et sommets
            arg_perm_sommets = self.perm_sommets * autre.perm_sommets
            arg_perm_aretes = self.perm_aretes * autre.perm_aretes

            # On calcule les nouveaux vecteurs orientations grâce à la loi de composition du produit semi-direct
            arg_vect_sommets = self.vect_sommets + self.perm_sommets * autre.vect_sommets
            arg_vect_aretes = self.vect_aretes + self.perm_aretes * autre.vect_aretes

            # On retourne le mouvement qui rassemble toutes les caractéristiques calculées précédemment :
            return Mouvement(arg_perm_sommets, arg_vect_sommets, arg_perm_aretes, arg_vect_aretes)

        else:
            return NotImplemented
    
    def __str__(self) -> str:
        """Méthode permettant de donner la représentation sous forme de chaîne de caractère
        d'un mouvement du cube."""

        ch = "" # Chaîne vierge

        ch += "-" * 25 # Délimiteur du haut
        ch += "\n Permutation sur les sommets :\n" + self.perm_sommets.__str__() + "\n"
        ch += "Vecteur-orientation sur les sommets : " + self.vect_sommets.__str__() + "\n"
        ch += "Permutation sur les arêtes :\n" + self.perm_aretes.__str__() + "\n"
        ch += "Vecteur-orientation sur les arêtes : " + self.vect_aretes.__str__() + "\n"
        ch += "-" * 25 + "\n" # Délimiteur du bas

        return ch
