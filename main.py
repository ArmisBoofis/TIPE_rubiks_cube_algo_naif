from random import randint

from mouvement import Mouvement
from outils_permutations import Cycle
from vecteurs_orientation import VecteurOrientation

# ---------------------------------- DEFINITION DES MOUVEMENTS ELEMENTAIRES ----------------------------------

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
u, d, r, l, f, b = U * U * U, D * D * D, R * \
    R * R, L * L * L, F * F * F, B * B * B

# ---------------------------------- FONCTIONS UTILITAIRES ----------------------------------

def executer(ch: str) -> Mouvement:
    """Fonction prenant en paramètre une chaîne de caractères représentant
    un mouvement, et renvoyant l'objet de type <Mouvement> correspondant"""

    # On définit un dictionnaire qui associe à chaque lettre le mouvement associé
    mvt = {'U': U, 'D': D, 'R': R, 'L': L, 'F': F, 'B': B,
           'u': u, 'd': d, 'r': r, 'l': l, 'f': f, 'b': b}

    res = Id  # On initialise le mouvement à l'identité

    # On itère sur la chaîne, en éxécutant à chaque fois le mouvement correspondant au caractère courant
    try:
        for c in ch:
            res *= mvt[c]

        return res

    except KeyError:
        # La chaîne comporte des caractères non-autorisés
        raise ValueError(
            "La chaîne soumise comporte des caractères interdits.")

def inverser(ch: str) -> str:
    """Fonction prenant en paramètre une chaîne de caractères représentant
    un mouvement, et qui renvoie la chaîne de caractère représentant le mouvement
    inverse."""

    return ch.swapcase()[::-1]

def melange() -> Mouvement:
    """Fonction qui génère une suite aléatoire de mouvements élémentaires, et qui retourne
    le mouvement global correspondant."""

    ch = "" # La chaîne de caractères correspond aux mouvements qui vont être effectués

    for _ in range(randint(25, 50)):
        ch += "UDLRBF"[randint(0, 5)]
    
    return executer(ch)

def mvt_phase_1(c1: int, c2: int) -> str:
    """Renvoie un mouvement qui envoie 3 sur c1 et 8 sur c2 ; permet la conjugaison
    de la phase 1 de l'algorithme."""

    if isinstance(c1, int) and isinstance(c2, int) and 1 <= c1 <= 8 and 1 <= c2 <= 8 and c1 != c2:
        # si c1 <= 4 et c2 <= 4, mvt1[c1][c2] contient un mouvement qui envoie 3 sur c1 et 8 sur c2
        mvt1 = [
            [],
            ['', '', 'UURR', 'UUDBB', 'UUBB'],
            ['', 'UDLL', '', 'UDBB', 'UBB'],
            ['', 'dFF', 'DDFF', '', 'DDLL'],
            ['', 'udFF', 'uDDFF', 'udRR', ''],
        ]

        # si c1 >= 5 et c2 >= 5, mvt2[c1][c2] contient un mouvement qui envoie 3 sur c1 + 4 et 8 sur c2 + 4
        mvt2 = [
            [],
            ['', '', 'BBUUFF', 'BBURR', 'UULL'],
            ['', 'UFFrBB', '','UFFBRR', 'UFF'],
            ['', 'RRULL', 'RRUL', '', 'RRub'],
            ['', 'b', 'bl', 'blf', ''],
        ]

        # on fait la grande disjonction de cas pour déterminer le mouvement à effectuer
        if c1 <= 4 and c2 >= 5:
            # cas le plus simple, on peut bouger les deux coins indépendamment
            prefixe = ['', 'UU', 'U', '', 'u']
            sufixe = ['', 'D', 'DD', 'd', '']

            return prefixe[c1] + sufixe[c2 - 4]
        
        elif c1 >= 5 and c2 <= 4:
            # cas similaire au précédent, un peu plus compliqué
            prefixe = ['', 'BB', 'BBD', 'UrB', 'bL']
            sufixe = ['', 'u', 'UU', 'U', '']

            return prefixe[c1 - 4] + sufixe[c2]

        elif c1 <= 4 and c2 <= 4:
            # cas plus compliqué, on a fait la disjonction de cas dans le tableau mvt1
            return mvt1[c1][c2]
        
        else:
            # on a fait la disjonction de cas dans le tableau mvt2
            return mvt2[c1 - 4][c2 - 4]
    
    else:
        return ValueError("Les valeurs données pour les coins c1 et c2 ne sont pas valides.")

# ---------------------------------- ALGORITHME DE RÉSOLUTION ----------------------------------

# On se donne une configuration initiale
configuration = melange()

print("Configuration initiale :")
print(configuration)

sol = "" # Chaîne de caractère qui représente la solution trouvée

# PHASE 1 : placement des sommets

# Ce mouvement permute seulement les sommets 3 et 8 en laissant les autres inchangés
M0, M0_txt = (D * R * d * r * F) ** 3, 'DRdrFDRdrFDRdrF'

# On parcourt les transpositions en sens inverse, en vue de calculer la permutation inverse
for transposition in configuration.perm_sommets.produit_transpositions:
    c1, c2 = transposition.representation_cycle[0], transposition.representation_cycle[1] # on veut envoyer 3 sur c1 et 8 sur c2

    # Mouvement qui permet la conjugaison
    M_txt = mvt_phase_1(c1, c2)
    Mi_txt = inverser(M_txt)

    # On applique le mouvement conjugé à la configuration actuelle
    configuration *= executer(Mi_txt) * M0 * executer(M_txt)
    sol += Mi_txt + M0_txt + M_txt

print("Configuration après le positionnement des sommets :")
print("Solution pour le moment : ", sol)