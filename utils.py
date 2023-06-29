"""Ce fichier contient quelques fonctions utilitaires, notamment concernant la manipulation
de chaînes de caractères représentant des mouvements."""

from random import randint

from mouvements_elementaires import *


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


def melange(n: int) -> Mouvement:
    """Fonction qui génère une suite aléatoire de mouvements
    élémentaires de taille <n>, et qui retourne le mouvement global correspondant."""

    ch = ""  # La chaîne de caractères correspond aux mouvements qui vont être effectués

    for _ in range(n):
        ch += "UDLRBFudlrbf"[randint(0, 11)]

    return executer(ch)
