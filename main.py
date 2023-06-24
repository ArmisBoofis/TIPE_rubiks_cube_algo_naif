from mouvement import Mouvement
from outils_permutations import Cycle, Permutation
from vecteurs_orientation import VecteurOrientation

# DEFINITION DES MOUVEMENTS ELEMENTAIRES

# Mouvement identité
Id = Mouvement(
    Cycle((), 8), # Permutation sur les sommets
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0], 3), # Vecteur orientation sur les sommets
    Cycle((), 12), # Permutation sur les arêtes
    VecteurOrientation([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2) # Vecteur orientation sur les arêtes
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
u, d, r, l, f, b = U * U * U, D * D * D, R * \
    R * R, L * L * L, F * F * F, B * B * B

# FONCTIONS UTILITAIRES

def executer(ch: str) -> Mouvement:
    """Fonction prenant en paramètre une chaîne de caractères représentant
    un mouvement, et renvoyant l'objet de type <Mouvement> correspondant"""

    # On définit un dictionnaire qui associe à chaque lettre le mouvement associé
    mvt = {'U': U, 'D': D, 'R': R, 'L': L, 'F': F, 'B': B,
           'u': u, 'd': d, 'r': r, 'l': l, 'f': f, 'b': b}

    res = Id # On initialise le mouvement à l'identité

    # On itère sur la chaîne, en éxécutant à chaque fois le mouvement correspondant au caractère courant
    try:
        for c in ch:
            res *= mvt[c]
        
        return res
    
    except KeyError:
        # La chaîne comporte des caractères non-autorisés
        raise ValueError("La chaîne soumise comporte des caractères interdits.")

print(executer('UR'))