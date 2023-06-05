
class Permutation:
    def __init__(self, images: list[int]):
        images.insert(0, 0) # Permet d'éviter les problèmes d'indice, puisqu'on compte à partir de 1

        if not Permutation._est_valide(images):
            raise ValueError("La liste donnée ne définit pas une permutation valide.")

        self._images = images
    
    def inverse(self):
        """Renvoie l'inverse de la permutation"""

        images_inverse = [0] * (len(self._images) - 1)

        for k in range(1, len(self._images)):
            images_inverse[self._images[k] - 1] = k
        
        return Permutation(images_inverse)

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
# - accesseur et mutateur pour _images
# - décomposition en produit de cycles
# - décomposition en produit de transpositions
# - signature