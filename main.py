
"""Fichier principal, qui exploite l'algorithme de résolution pour en tirer
des courbes."""

import matplotlib.pyplot as plt

from resoudre import resoudre
from utils import melange

if __name__ == "__main__":
    longueur_entree = [k for k in range(1, 1000)]
    resultats, moyenne = [], 0

    for s in longueur_entree:
        # On regarde en combien de mouvements l'algorithme résout une configuration mélangée avec <l> mouvements
        nb_coups = len(resoudre(melange(s)))

        resultats.append(nb_coups)
        moyenne += nb_coups

    moyenne /= 1000

    plt.plot(longueur_entree, resultats, 'ob', markersize=3, label="Nombre de coups mis par l'algorithme")
    plt.axhline(y = moyenne, color = 'r', linestyle="--", label="Nombre moyen de coups mis par l'algorithme")

    plt.xlabel('Nombre de coups pour mélanger')
    plt.ylabel('Nombre de coups pour résoudre')

    plt.legend()
    plt.title("Résultats pratiques de l'algorithme théorique")

    plt.show()