"""Ce fichier contient la définition de tous les mouvements élémentaires, ainsi que de leurs inverses."""

from mouvement import Mouvement
from outils_permutations import Cycle
from vecteurs_orientation import VecteurOrientation

# Mouvement identité
Id = Mouvement(
    Cycle((), 8),  # Permutation sur les sommets
    # Vecteur orientation sur les sommets
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0], 3),
    Cycle((), 12),  # Permutation sur les arêtes
    # Vecteur orientation sur les arêtes
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2)
)

# Mouvement "up"
U = Mouvement(
    Cycle((1, 4, 3, 2), 8),
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0], 3),
    Cycle((1, 2, 3, 4), 12),
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2)
)

# Mouvement "down"
D = Mouvement(
    Cycle((5, 6, 7, 8), 8),
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0], 3),
    Cycle((11, 10, 9, 12), 12),
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2)
)

# Mouvement "right"
R = Mouvement(
    Cycle((2, 3, 8, 7), 8),
    VecteurOrientation([0, 1, 2, 0, 0, 0, 2, 1], 3),
    Cycle((7, 2, 6, 10), 12),
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2)
)

# Mouvement "left"
L = Mouvement(
    Cycle((4, 1, 6, 5), 8),
    VecteurOrientation([2, 0, 0, 1, 2, 1, 0, 0], 3),
    Cycle((4, 8, 12, 5), 12),
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2)
)

# Mouvement "front"
F = Mouvement(
    Cycle((1, 2, 7, 6), 8),
    VecteurOrientation([1, 2, 0, 0, 0, 2, 1, 0], 3),
    Cycle((3, 7, 11, 8), 12),
    VecteurOrientation([0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0], 2)
)

# Mouvement "back"
B = Mouvement(
    Cycle((3, 4, 5, 8), 8),
    VecteurOrientation([0, 0, 1, 2, 1, 0, 0, 2], 3),
    Cycle((1, 5, 9, 6), 12),
    VecteurOrientation([1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0], 2)
)

# Mouvement inverses : correspond à chaque fois au mouvement élémentaire itéré trois fois
u, d, r, l, f, b = U ** 3, D ** 3, R ** 3, L ** 3, F ** 3, B ** 3
