"""Ce fichier contient l'algorithme de résolution du Rubik's Cube."""

import json

from mouvements_elementaires import *
from utils import executer, inverser

# Chargement des tableaux contenant les mouvements de conjugaison
with open('mouvements_conjugaison.json', 'r') as fichier:
    mvt_conjugaison = json.load(fichier)


def resoudre(configuration: Mouvement) -> str:
    """Fonction qui prend en paramètre un mouvement et qui renvoie une
    suite de mouvements élémentaires qui correspond à son inverse."""

    sol = ""  # Chaîne de caractère qui représente la solution trouvée

    # PHASE 1 : placement des sommets

    # Ce mouvement permute seulement les sommets 3 et 8 en laissant les autres inchangés
    M0, M0_txt = (D * R * d * r * F) ** 3, 'DRdrFDRdrFDRdrF'

    # On parcourt les transpositions en sens inverse, en vue de calculer la permutation inverse
    for transposition in configuration.perm_sommets.produit_transpositions:
        # on veut envoyer 3 sur c1 et 8 sur c2
        c1, c2 = transposition.representation_cycle[0], transposition.representation_cycle[1]

        # Mouvement qui permet la conjugaison
        M_txt = mvt_conjugaison['phase_1'][c1][c2]
        Mi_txt = inverser(M_txt)

        # On applique le mouvement conjugé à la configuration actuelle
        configuration *= executer(Mi_txt) * M0 * executer(M_txt)
        sol += Mi_txt + M0_txt + M_txt

    # PHASE 2 : orientation des sommets

    # Ce mouvement ne change pas le positionnement des sommets, et change l'orientation des sommets 7 et 8
    M0, M0_txt = (D * r) ** 3 * (d * R) ** 3, 'DrDrDrdRdRdR'
    i1, i2 = 0, 1  # Indices utilisés pour parcourir les composantes du vecteur orientation sur les sommets

    # On repète les ré-orientations jusqu'à ce que tous les coins soient bien orientés
    while i1 < 7:
        # On récupère la liste des composantes du vecteur orientation sur les sommets actuel
        vect = configuration.vect_sommets.valeurs

        if vect[i1] == 0:
            i1 += 1

        elif vect[i2] == 0 or i2 <= i1:
            i2 += 1

        else:
            # on a i1 < i2 et vect[i1] != 0 et vect[i2] != 0
            # on calcule le mouvement par lequel on va conjuguer M0
            M_txt = mvt_conjugaison['phase_2'][i1 + 1][i2 + 1]
            Mi_txt = inverser(M_txt)

            # on multiplie enfin <configuration> par <M0> conjugé par <M>
            configuration *= executer(Mi_txt) * M0 * executer(M_txt)
            sol += Mi_txt + M0_txt + M_txt

    # PHASE 3 : placement des arêtes

    # Ce mouvement permute trois arêtes (selon un 3-cycle) et laisse tous les autres cubes inchangés
    M0, M0_txt = L * r * U ** 2 * l * R * B ** 2, 'LrUUlRBB'

    # Pour chaque trois-cycle qui compose la permutation sur les arêtes de la configuration, on calcule un mouvement qui l'inverse par conjugaison
    for trois_cycle in configuration.perm_aretes.produit_trois_cycles:
        c1, c2, c3 = trois_cycle.representation_cycle[
            0], trois_cycle.representation_cycle[1], trois_cycle.representation_cycle[2]

        # Mouvement qui permet la conjugaison
        M_txt = mvt_conjugaison['phase_3'][c3][c2][c1]
        Mi_txt = inverser(M_txt)

        # On multiplie <configuration> par <M0> conjugué par <M>
        configuration *= executer(Mi_txt) * M0 * executer(M_txt)
        sol += Mi_txt + M0_txt + M_txt

    # PHASE 4 : orientation des arêtes

    # Le mouvement suivant change l'orientation de deux arêtes en laissant les autres cubes inchangés
    M0_txt = 'LrFLrDLrBLrULrfLrdLrbLru'
    M0 = executer(M0_txt)

    # Indices utilisés pour parcourir le vecteur orientation sur les arêtes
    i1, i2 = 0, 1

    # On répète les ré-orientations jusqu'à ce que toutes les arêtes soient bien orientées
    while i1 < 11:
        # Composantes du vecteur orientation sur les arêtes
        vect = configuration.vect_aretes.valeurs

        if vect[i1] == 0:
            i1 += 1

        elif vect[i2] == 0 or i2 <= i1:
            i2 += 1

        else:
            # on calcule le mouvement par lequel on va conjuguer <M0>
            M_txt = mvt_conjugaison['phase_4'][i1 + 1][i2 + 1]
            Mi_txt = inverser(M_txt)

            # on multiplie la configuration actuelle par le mouvement conjugué
            configuration *= executer(Mi_txt) * M0 * executer(M_txt)
            sol += Mi_txt + M0_txt + M_txt

    return sol
