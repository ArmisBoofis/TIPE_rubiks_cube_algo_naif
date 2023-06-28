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
u, d, r, l, f, b = U ** 3, D ** 3, R ** 3, L ** 3, F ** 3, B ** 3

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

    ch = ""  # La chaîne de caractères correspond aux mouvements qui vont être effectués

    for _ in range(randint(25, 50)):
        ch += "UDLRBF"[randint(0, 5)]

    return executer(ch)


def mvt_phase_1(c1: int, c2: int) -> str:
    """Renvoie un mouvement qui envoie le sommet 3 sur le sommet c1 et le sommet 8 sur le
    sommet c2 ; permet la conjugaison de la phase 1 de l'algorithme."""

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
            ['', 'UFFrBB', '', 'UFFBRR', 'UFF'],
            ['', 'RRULL', 'RRUL', '', 'RRub'],
            ['', 'b', 'bl', 'blf', ''],
        ]

        # on fait la grande disjonction de cas pour déterminer le mouvement à effectuer
        if c1 <= 4 and c2 >= 5:
            # cas le plus simple, on peut bouger les deux coins indépendamment
            prefixe = ['', 'UU', 'U', '', 'u']
            suffixe = ['', 'D', 'DD', 'd', '']

            return prefixe[c1] + suffixe[c2 - 4]

        elif c1 >= 5 and c2 <= 4:
            # cas similaire au précédent, un peu plus compliqué
            prefixe = ['', 'BB', 'BBD', 'UrB', 'bL']
            suffixe = ['', 'u', 'UU', 'U', '']

            return prefixe[c1 - 4] + suffixe[c2]

        elif c1 <= 4 and c2 <= 4:
            # cas plus compliqué, on a fait la disjonction de cas dans le tableau mvt1
            return mvt1[c1][c2]

        else:
            # on a fait la disjonction de cas dans le tableau mvt2
            return mvt2[c1 - 4][c2 - 4]

    else:
        return ValueError("Les valeurs données pour les coins c1 et c2 ne sont pas valides.")


def mvt_phase_2(c1: int, c2: int) -> str:
    """Renvoie un mouvement qui envoie le sommet 8 sur c1 et le sommet 7 sur c2,
    ce qui permet la conjugaison de la phase 2 de l'algorithme."""

    # Premier tableau qui donne la première partie du mouvement à effectuer
    prefixe = ['', 'DLL', 'RR', 'r', 'BB', 'D', 'DD', 'd', '']

    # Deuxième tableau qui donne la deuxième partie du mouvement à effectuer
    suffixe = [
        [],
        ['', '', 'RR', 'B', 'rB', 'D', 'DD', 'd', ''],
        ['', 'BL', '', '', 'B', 'BB', 'BLL', 'bd', 'b'],
        ['', 'DLL', 'df', '', 'DL', 'D', 'DD', 'd', ''],
        ['', 'FF', 'f', 'RR', '', 'DD', 'd', '', 'D'],
        ['', 'RFF', 'RR', 'r', 'ru', '', 'RF', 'R', ''],
        ['', 'bu', 'BRR', 'BB', 'b', '', '', 'BR', 'B'],
        ['', 'l', 'lu', 'lUU', 'LL', 'L', '', '', 'LB'],
        ['', 'FF', 'f', 'fu', 'FFU', 'FL', 'F', '', '']
    ]

    # on renvoie ensuite la solution complète
    return prefixe[c1] + suffixe[c1][c2]


def mvt_phase_3(c1: int, c2: int, c3: int) -> str:
    """Renvoie un mouvement qui envoie l'arête 1 sur c1, l'arête 3 sur c2, et l'arête 9 sur c3.
    Permet la conjugaison du mouvement de la phase 3."""

    # On a calculé (pas à la main !), le tableau à trois dimensions qui donne le résultat voulu
    return [[], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', 'DlFR', 'ulbL', 'ulb', 'Brub', 'FdR', 'DDFR', 'FR', 'FRd', 'DFDR', 'DFR'], ['', '', 'Brb', '', 'DLL', 'DL', 'dr', 'dR', 'Dl', 'R', 'd', 'DD', 'D'], ['', '', 'URBr', 'DflF', '', 'Ulbu', 'URB', 'UdRB', 'Dfl', 'fl', 'dfl', 'Dlfl', 'flD'], ['', '', 'UDlFu', 'UDluF', 'DfLL', '', 'URUB', 'UdRUB', 'UDlu', 'Ulu', 'Udlu', 'UDDlu', 'UlDu'], ['', '', 'FdRR', 'DlFRR', 'UlBBu', 'ulub', '', 'FRdR', 'DDFRR', 'FRR', 'FRRd', 'DDuRU', 'DFRR'], ['', '', 'Burb', 'DlF', 'DDFl', 'DLF', 'drF', '', 'DDF', 'F', 'Fd', 'DFD', 'DF'], ['', '', 'DDfR', 'dRf', 'DLLf', 'DLf', 'drf', 'DDf', '', 'f', 'df', 'Dlf', 'Df'], ['', '', 'URlBr', 'DlFrD', 'UBlBu', 'DfLd', 'URlB', 'fLdR', 'FrDl', '', 'fLd', 'DFrD', 'FrD'], ['', '', 'BFrb', 'DlFr', 'DDFrl', 'DLFr', 'Fdr', 'DFDrf', 'DDFr', 'Fr', '', 'DFDr', 'DFr'], ['', '', 'DDfRf', 'DDFF', 'DDFlF', 'DLFF', 'FdFr', 'DlFF', 'DFDF', 'FF', 'FdF', '', 'DFF'], ['', '', 'DDfRL', 'dRfL', 'DLfL', 'DfL', 'BfLU', 'DDfL', 'UlDul', 'fL', 'FFd', 'DlfL', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', 'UDlFb', 'UlbL', 'Ulb', 'URBU', 'UUFdR', 'UDlb', 'flU', 'Udlb', 'UDDlb', 'UlDb'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'brb', '', '', 'bLr', 'br', 'dbr', 'FdRU', 'Dlbr', 'ULF', 'ULFd', 'DDbr', 'Dbr'], ['', 'UBB', '', 'DlUF', '', 'Ub', 'UB', 'dRU', 'DlU', 'U', 'Ud', 'UDD', 'UD'], ['', 'UBBl', '', 'UDlF', 'DlUl', '', 'UBl', 'dRUl', 'UDl', 'Ul', 'Udl', 'UDDl', 'UlD'], ['', 'UlBB', '', 'UUbLu', 'UUbuL', 'UUbu', '', 'FRdRU', 'UDlBB', 'FRRU', 'UUdbu', 'UUDDbu', 'UUDbu'], ['', 'FUBB', '', 'bLur', 'DlFU', 'FUb', 'FUB', '', 'DDFU', 'FU', 'FUd', 'DFUD', 'DFU'], ['', 'UDLb', '', 'DDfRU', 'UbL', 'UDL', 'ULB', 'DDfU', '', 'UL', 'ULd', 'UDDL', 'ULD'], ['', 'UBlB', '', 'UDlBF', 'UUBBu', 'FbrD', 'UlB', 'dRUlB', 'UDlB', '', 'ULLd', 'UDDlB', 'UlDB'], ['', 'Fbrb', '', 'DlFbr', 'FbLr', 'Fbr', 'UlBd', 'UUFdbR', 'UDlBd', 'FrU', '', 'ULDfD', 'ULfD'], ['', 'UDLbf', '', 'DDFUF', 'UbLf', 'UDLf', 'ULBf', 'UDDLf', 'ULDfl', 'ULf', 'ULdf', '', 'ULDf'], ['', 'UDLbL', '', 'UDlFl', 'UDLL', 'ULDL', 'ULLB', 'DDfUL', 'UlDl', 'ULL', 'ULdL', 'UDDLL', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'UBUr', '', 'UbUL', 'UbU', 'UBU', 'UUdR', 'UUDl', 'UU', 'UUd', 'UUDD', 'UUD'], ['', 'BLuB', '', '', 'BLBu', 'UUbr', 'BLu', 'BRRLu', 'UDlbU', 'uLF', 'BRLu', 'DDBLu', 'uLDF'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'bLrU', 'UBrf', '', '', 'brU', 'UUBL', 'UDDrf', 'ULUDl', 'Urf', 'Urdf', 'UDrfD', 'UDrf'], ['', 'UBUB', 'UUBr', '', 'UDlFU', '', 'UUB', 'UUBRR', 'UDlU', 'UlU', 'UUBR', 'UUDDB', 'UUDB'], ['', 'UbUb', 'UBUrb', '', 'UUbL', 'UUb', '', 'udRu', 'UUDlb', 'uRu', 'UUdb', 'UUDDb', 'UUDb'], ['', 'uBru', 'BLur', '', 'DBLLF', 'FUUb', 'BLLF', '', 'DDFUU', 'FUU', 'FUUd', 'DDuru', 'DFUU'], ['', 'UbLU', 'UDLbU', '', 'brUL', 'UDLU', 'ULUB', 'ULUdR', '', 'ULU', 'ULUd', 'UDDLU', 'ULUD'], ['', 'UUBB', 'UUBrB', '', 'UUbLb', 'uRub', 'UlUB', 'udRub', 'UDlUB', '', 'UUBRB', 'UUDDBB', 'UUDBB'], ['', 'UUBBd', 'BLLFr', '', 'UUbRL', 'UUbR', 'UlUBd', 'UUdbR', 'UUDlbR', 'FUUr', '', 'UUDDbR', 'UUDbR'], ['', 'UbLfU', 'ULBrf', '', 'UrbLf', 'UUbRd', 'UUBlD', 'UUdbRd', 'UUDBlD', 'ULrf', 'ULdfU', '', 'ULULD'], ['', 'UUBBD', 'UUBrl', '', 'UDLUL', 'ULUDL', 'UUBl', 'UUBRRl', 'UUDBl', 'ULUL', 'UUBRl', 'UUDDBl', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'uRBr', 'UBrfU', '', 'ulbu', 'uRB', 'FdRu', 'UUDfl', 'FRu', 'FRud', 'DDuRB', 'DFRu'], ['', 'uBB', '', 'DLLu', '', 'ub', 'uB', 'dRu', 'Dlu', 'u', 'ud', 'DDu', 'Du'], ['', 'BLB', 'BLr', '', '', 'DBL', 'BL', 'BRRL', 'Dflu', 'BLb', 'BRL', 'DDBL', 'DFuf'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'uRBB', 'UUBUr', 'UUBrU', '', '', 'UUBU', 'FdRuB', 'UDlUU', 'UlUU', 'UUBUR', 'UUDDBU', 'UUDBU'], ['', 'uBBR', 'dRuR', 'udRf', '', 'ubR', '', 'udR', 'DluR', 'uR', 'uRd', 'DDuR', 'DuR'], ['', 'BLBF', 'uBr', 'DDFlu', '', 'Fub', 'BLF', '', 'DDFu', 'Fu', 'Fud', 'DDur', 'DFu'], ['', 'BULB', 'BULr', 'BrUL', '', 'fub', 'BUL', 'DDfu', '', 'fu', 'dfu', 'Dlfu', 'Dfu'], ['', 'ubRb', 'UUBBU', 'udRbf', '', 'uRb', 'BfLd', 'udRb', 'DluRb', '', 'uRdb', 'DDuRb', 'DuRb'], ['', 'BLBFr', 'BLFr', 'BFrUL', '', 'Furb', 'Fudr', 'uRdR', 'DDFur', 'Fur', '', 'DDuRR', 'DFur'], ['', 'BULBf', 'uBrF', 'DDFuF', '', 'FFub', 'BULf', 'DlFFu', 'DDurF', 'FFu', 'FudF', '', 'DFFu'], ['', 'BfLB', 'BrfL', 'DLfLu', '', 'DBfL', 'BfL', 'DDBfL', 'UUDBlU', 'fLu', 'BRfL', 'DBfDL', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'BUUr', 'BUrU', 'BrUU', '', 'BUU', 'BUURR', 'Dulu', 'ulu', 'BUUR', 'DDBUU', 'DBUU'], ['', 'Bru', '', 'DulF', 'Dlul', '', 'Bu', 'BRRu', 'Dul', 'ul', 'BRu', 'DDBu', 'DBu'], ['', 'drB', 'Br', '', 'DLLB', '', 'B', 'BRR', 'DlB', 'DLB', 'BR', 'DDB', 'DB'], ['', 'URBB', 'BUr', 'BrU', '', '', 'BU', 'BURR', 'DlBU', 'ful', 'BUR', 'DDBU', 'DBU'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'BruR', 'FrBr', 'DuRlF', 'DluRl', '', '', 'BRuR', 'DuRl', 'uRl', 'BuR', 'BuRd', 'DBuR'], ['', 'Buru', 'Bur', 'DlBF', 'DDFul', '', 'BF', '', 'DDBF', 'Ful', 'BRF', 'DBFD', 'DBF'], ['', 'Brfu', 'Brf', 'BRRf', 'URbDL', '', 'Bf', 'DDBf', '', 'DLBf', 'BRf', 'DBfD', 'DBf'], ['', 'URUBB', 'BFrD', 'BFrUD', 'DfLLB', '', 'UluB', 'BFrDr', 'UDluB', '', 'UdluB', 'DBFrD', 'uRbl'], ['', 'BFru', 'BFr', 'BFrU', 'BFrUU', '', 'FrB', 'BuRR', 'DDBFr', 'Furl', '', 'DBFDr', 'DBFr'], ['', 'BFFru', 'BFFr', 'DDBFF', 'URbDLf', '', 'BFF', 'DBfDf', 'DBFDF', 'FFul', 'BRFF', '', 'DBFF'], ['', 'BBDfL', 'fLBr', 'dRfLB', 'DLfLB', '', 'fLB', 'DDfLB', 'UUDBUl', 'DfLB', 'FFdB', 'DBlfL', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'bLUU', 'buLu', 'bUUL', 'bUU', '', 'UdRU', 'UDRUl', 'URU', 'URUd', 'UDDRU', 'UDRU'], ['', 'ulBB', '', 'bLu', 'buL', 'bu', '', 'FUdR', 'Dlbu', 'FUR', 'dbu', 'DDbu', 'Dbu'], ['', 'DLb', 'BrBB', '', 'bL', 'b', '', 'dRb', 'Dlb', 'URu', 'db', 'DDb', 'Db'], ['', 'bLU', 'DLbU', 'UdRf', '', 'bU', '', 'UdR', 'DlUR', 'UR', 'URd', 'UDDR', 'UDR'], ['', 'bLUl', 'DLbUl', 'UDRlF', 'fLbL', '', '', 'UdRl', 'UDRl', 'URl', 'URdl', 'bUlD', 'bUl'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'DLFb', 'DLFbU', 'DlFb', 'FbL', 'Fb', '', '', 'DDFb', 'URuF', 'Fdb', 'DFDb', 'DFb'], ['', 'DLbf', 'DDfUR', 'dRbf', 'bUL', 'bf', '', 'ULdR', '', 'URL', 'dbf', 'Dlbf', 'Dbf'], ['', 'UBlBR', 'BBUlB', 'bfLud', 'bfLd', 'FRRb', '', 'ULLdR', 'UDlBR', '', 'UlBR', 'DFrbD', 'URblB'], ['', 'UlBBR', 'BFrBB', 'DlFrb', 'FrbL', 'Frb', '', 'UUdbuR', 'DDFrb', 'Fdrb', '', 'UlBRd', 'DFrb'], ['', 'DLFFb', 'UDDLfR', 'ULdRf', 'FFbL', 'FFb', '', 'ULdfR', 'DFDFb', 'URLf', 'FdFb', '', 'DFFb'], ['', 'DfLb', 'DfLbU', 'bfLu', 'bfL', 'fLb', '', 'ULdRL', 'bULL', 'URLL', 'FFdb', 'DlbfL', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'URBUr', 'UBrU', 'UrlbL', 'Urlb', 'UBUF', '', 'UUDDF', 'UUF', 'UUFd', 'UUDFD', 'UUDF'], ['', 'UlBBr', '', 'bRRLu', 'UBrUU', 'bRRu', 'BLuF', '', 'UUDDFU', 'UUFU', 'UUFUd', 'dbRFR', 'UUDFU'], ['', 'UBru', 'dbRR', '', 'bRRL', 'bRR', 'Udru', '', 'UDrul', 'Uru', 'Urud', 'UDDru', 'UDru'], ['', 'UBBr', 'UBr', 'DlUFr', '', 'Urb', 'Udr', '', 'DlUr', 'Ur', 'Urd', 'UDDr', 'UDr'], ['', 'UBUBF', 'UBrl', 'UDlUF', 'DlUrl', '', 'UUBF', '', 'UDrl', 'Url', 'Urdl', 'UDDrl', 'UrlD'], ['', 'UrlBB', 'UlBdr', 'UBrUb', 'UUFbL', 'UUFb', '', '', 'UUDDFb', 'FrUr', 'UUFdb', 'udRuF', 'UUDFb'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'UDLrb', 'ULBr', 'ULBrU', 'UrbL', 'UDLr', 'ULdr', '', '', 'ULr', 'ULrd', 'UDDLr', 'ULDr'], ['', 'UUBBF', 'UlBr', 'UlBrU', 'UUBBFu', 'FUrDL', 'UrlB', '', 'UDrlB', '', 'ULLrd', 'DFUrD', 'FUrD'], ['', 'FUBBr', 'FUBr', 'FUBrU', 'DlFUr', 'FUrb', 'FUdr', '', 'DDFUr', 'FUr', '', 'DFUDr', 'DFUr'], ['', 'uBruF', 'ULBfr', 'ULBfrU', 'UbLfr', 'UDLfr', 'ULdfr', '', 'ULDfrl', 'ULfr', 'FUrd', '', 'ULDfr'], ['', 'UUBBDF', 'ULLBr', 'UUDBlF', 'UDLLr', 'ULDLr', 'UUBFl', '', 'UrlDl', 'ULLr', 'ULrdL', 'FUrDD', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'UBUrf', 'ubLu', 'UbULf', 'UbUf', 'UBUf', 'UUDDf', '', 'UUf', 'UUdf', 'UUDlf', 'UUDf'], ['', 'DuLb', '', 'DLLuL', 'ubL', 'DuL', 'uLB', 'dRuL', '', 'uL', 'uLd', 'DDuL', 'uLD'], ['', 'BLLB', 'BLLr', '', 'DBLL', 'DuLU', 'BLL', 'BRRLL', '', 'uLU', 'BRLL', 'DDBLL', 'uLUD'], ['', 'DBLLU', 'UBrFF', 'BLLrU', '', 'brUf', 'BLLU', 'UUDDfu', '', 'UUfu', 'UUdfu', 'DBlfl', 'UUDfu'], ['', 'UBUBf', 'UUBrf', 'BrlUl', 'DBlUl', '', 'UUBf', 'UUDDBf', '', 'UlUf', 'UUBRf', 'UDlUf', 'UUDBf'], ['', 'UbUbf', 'dRuRL', 'udRuf', 'ubRL', 'UUbf', '', 'uLdR', '', 'uRL', 'uRLd', 'DDuRL', 'uRLD'], ['', 'DFuLb', 'uLBr', 'DBlDF', 'FubL', 'DFuL', 'BLFL', '', '', 'FuL', 'FuLd', 'DDuLr', 'FuLD'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'UUBBf', 'UUBBUL', 'uRbLu', 'uRbL', 'uRLb', 'UlUBf', 'uLdRb', '', '', 'fuLd', 'dfuLd', 'FuLrD'], ['', 'UUBBdf', 'BLFLr', 'UUdbRf', 'FurbL', 'UUbRf', 'FuLdr', 'uRLdR', '', 'FuLr', '', 'fuLDD', 'ULUfD'], ['', 'UbLUf', 'uBrFL', 'ULUdRf', 'FFubL', 'UDLUf', 'ULUBf', 'UDDLUf', '', 'ULUf', 'ULUdf', '', 'fuLD'], ['', 'DfuLb', 'BULLr', 'BrULL', 'fubL', 'DfuL', 'BULL', 'DDfuL', '', 'fuL', 'dfuL', 'DlfuL', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'BUBU', 'BBUU', 'BuBu', 'URlb', 'uRlB', 'UdRlb', 'UDRlb', '', 'BuRB', 'BuRdB', 'bUlb'], ['', 'BuB', '', 'bLub', 'BBu', 'BBul', 'ulB', 'BRRBu', 'DulB', '', 'BRBu', 'DDBBu', 'DBBu'], ['', 'BB', 'BrB', '', 'bLb', 'bRD', 'Bld', 'BRRB', 'DBBl', '', 'BRB', 'DDBB', 'DBB'], ['', 'BUB', 'BBU', 'BrUB', '', 'URb', 'BBUR', 'UdRb', 'DBBlU', '', 'URdb', 'UDDRb', 'UDRb'], ['', 'BUUB', 'BBUl', 'BUrUB', 'BUUBu', '', 'BUld', 'UdRbl', 'UDRbl', '', 'URdbl', 'BURld', 'URbl'], ['', 'BuBR', 'BFrDB', 'BBuRu', 'BBuR', 'URUb', '', 'UdRUb', 'DulBR', '', 'ulBR', 'DbuRD', 'UDRUb'], ['', 'BBF', 'BBFU', 'DBBlF', 'BBFu', 'bRDF', 'BFld', '', 'DDBBF', '', 'BRBF', 'DBFDB', 'DBBF'], ['', 'BBf', 'BBUL', 'URbLu', 'URbL', 'URLb', 'Bldf', 'ULdRb', '', '', 'BRBf', 'DBBlf', 'DBBf'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'BBFr', 'BFrB', 'BFrUB', 'BBFur', 'URUbR', 'BRBFr', 'BBFUr', 'DDBBFr', '', '', 'UlBRdb', 'DBBFr'], ['', 'BBFF', 'BBULf', 'URbLfu', 'URbLf', 'URLbf', 'BFldF', 'ULdfRb', 'URbLuf', '', 'BRBFF', '', 'DBBFF'], ['', 'BBfL', 'BBULL', 'bfLub', 'bfLb', 'URLLb', 'DfLBB', 'ULdRLb', 'URbLL', '', 'BRBfL', 'URbLLf', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'UBUFr', 'UBrUr', 'BuBud', 'FbRu', 'UUFdr', 'URUdR', 'UUDDFr', 'UUFr', '', 'BuRBd', 'UUDFr'], ['', 'BuBd', '', 'bRLu', 'BBud', 'FbR', 'ulBd', 'FdbR', 'DDFbR', 'FbRB', '', 'DDbRu', 'DFbR'], ['', 'BBd', 'BrBd', '', 'bRL', 'bR', 'BBdb', 'dbR', 'DlbR', 'bRB', '', 'DDbR', 'DbR'], ['', 'BUBd', 'UdRR', 'URdRf', '', 'bUR', 'URRB', 'URdR', 'DlURR', 'URR', '', 'UDDRR', 'UDRR'], ['', 'BUUBd', 'UUBFr', 'UUBFrU', 'fLbRL', '', 'UUFrB', 'URdRl', 'UDRRl', 'URRl', '', 'bUlDR', 'bURl'], ['', 'BuBRd', 'FUdRR', 'bLuR', 'buRL', 'buR', '', 'dbuR', 'DlbuR', 'FURR', '', 'DDbuR', 'DbuR'], ['', 'BBFd', 'BLuFr', 'DlbRF', 'bRLF', 'bRF', 'BBFdb', '', 'DDbRF', 'bRBF', '', 'dbRF', 'DbRF'], ['', 'BBdf', 'ULdRR', 'dbRf', 'bURL', 'bRf', 'URRLB', 'dbfR', '', 'URRL', '', 'DlbRf', 'DbRf'], ['', 'buRb', 'UrlBr', 'bLuRb', 'buRLb', 'FURRb', 'URRlB', 'UlBRR', 'UDRRlB', '', '', 'UlBRRF', 'DbuRb'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'BBFdF', 'BFrBd', 'dbfRf', 'FFbRL', 'FFbR', 'FUrdr', 'FdFbR', 'dbRFF', 'URRLf', '', '', 'DFFbR'], ['', 'DfLbR', 'UUBFrl', 'dbRfL', 'bRfL', 'fLbR', 'UUFrBl', 'FFdbR', 'bURLL', 'URRLL', '', 'DlbRfL', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'URBUrF', 'UBrFU', 'UrFlbL', 'UrFlb', 'UBUFF', 'UBrUF', 'ubLuf', 'UUFF', 'UUFdF', '', 'UUDFF'], ['', 'DuLbf', '', 'dRuLf', 'ubLf', 'DuLf', 'BulD', 'DDuLf', 'DBulD', 'uLf', 'uLdf', '', 'uLDf'], ['', 'BBDD', 'BrlD', '', 'bRLd', 'bRd', 'BlD', 'dbRd', 'DBlD', 'ULrF', 'BlDR', '', 'BlbD'], ['', 'UBBrF', 'UBrF', 'DlUrF', '', 'UrFb', 'UdrF', 'URRdR', 'UDDrF', 'UrF', 'URRd', '', 'UDrF'], ['', 'URBBlD', 'UBrFl', 'UDrlF', 'UDDrFl', '', 'BUlD', 'UDlUFF', 'UDrFl', 'UrFl', 'URRdl', '', 'UrFbl'], ['', 'UrFlBB', 'UlBdrF', 'uLdRf', 'ubRLf', 'buRd', '', 'uLdfR', 'DBuRlD', 'uRLf', 'BulDR', '', 'uRLDf'], ['', 'UBruF', 'BurlD', 'DBlFD', 'ubLfr', 'bRRF', 'BFlD', '', 'DBFlD', 'UruF', 'UrudF', '', 'UDruF'], ['', 'BLLBf', 'UBrFL', 'dbRfd', 'UrFbL', 'bRfd', 'BLLf', 'dbfRd', '', 'UrFL', 'URRLd', '', 'BlbfD'], ['', 'BUlDB', 'UlBrF', 'UDrlBF', 'uRbLf', 'uRLbf', 'UrFlB', 'UlBrUF', 'UDrFlB', '', 'fuLdf', '', 'FUrDF'], ['', 'buRbd', 'BFlDr', 'DDFUrF', 'DlFUrF', 'FUrFb', 'BFFlD', 'UlBRRd', 'DBFFlD', 'FUrF', '', '', 'DFUrF'], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', 'BUlBD', 'ULLBrF', 'UDrlFl', 'bRfdL', 'DfuLf', 'BULLf', 'DlfuLf', 'UrFbLL', 'fuLf', 'dfuLf', '', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', 'BUUrl', 'DuLLu', 'UbUfL', 'UUDfL', 'BUUl', 'UUDDfL', 'DBUUl', 'UUfL', 'UUFFd', 'bUlbD', ''], ['', 'BuBD', '', 'DBulF', 'DuLL', 'uLDL', 'Bul', 'BRRul', 'DBul', 'uLL', 'BRul', 'DDBul', ''], ['', 'BBD', 'Brl', '', 'DlBl', 'BBDB', 'Bl', 'BRRl', 'DBl', 'Blb', 'BRl', 'DDBl', ''], ['', 'BUBD', 'BBUD', 'BrlU', '', 'URbD', 'BlU', 'UdRbD', 'DBlU', 'BlUb', 'UrFd', 'UDRbD', ''], ['', 'URBBl', 'BUrl', 'BrUl', 'DlBUl', '', 'BUl', 'BURRl', 'DBUl', 'fuLL', 'BURl', 'URblD', ''], ['', 'BuBDR', 'FrBrl', 'UUbfLu', 'UUbfL', 'UUfLb', '', 'BRuRl', 'DBuRl', 'uRLL', 'BuRl', 'BuRdl', ''], ['', 'BBDF', 'Burl', 'DBlF', 'DDBFl', 'BBDBF', 'BFl', '', 'DBFl', 'BFlb', 'BRFl', 'DBBFD', ''], ['', 'BBDf', 'Brlf', 'BRRlf', 'URbLD', 'URLbD', 'Blf', 'DDBlf', '', 'Blbf', 'BRlf', 'DBlf', ''], ['', 'BUlB', 'BUrlB', 'BrUlB', 'BUlBu', 'uRLLb', 'UluBl', 'BURRlB', 'DBUlB', '', 'BURlB', 'URblDB', ''], ['', 'BBDFr', 'BFrl', 'DBlFr', 'UUbRfL', 'UUfLbR', 'FrBl', 'BuRRl', 'DBFrl', 'BFlbr', '', 'DBBFDr', ''], ['', 'BBDFF', 'BFFrl', 'DBFlF', 'bfLbD', 'fuLDL', 'BFFl', 'DBlFF', 'DBFFl', 'ULUfL', 'BRFFl', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '']], [['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '']]][c1][c2][c3]

# ---------------------------------- ALGORITHME DE RÉSOLUTION ----------------------------------

# On se donne une configuration initiale
configuration = melange()

configuration_bis = configuration

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


print('Configuration après la phase 1 :')
print(configuration)

# PHASE 2 : orientation des sommets


M0, M0_txt = (D * r) ** 3 * (d * R) ** 3, 'DrDrDrdRdRdR' # Ce mouvement ne change pas le positionnement des sommets, et change l'orientation des sommets 7 et 8
i1, i2 = 0, 1 # Indices utilisés pour parcourir les composantes du vecteur orientation sur les sommets

# On repète les ré-orientations jusqu'à ce que tous les coins soient bien orientés
while i1 < 7:
    vect = configuration.vect_sommets.valeurs # On récupère la liste des composantes du vecteur orientation sur les sommets actuel

    if vect[i1] == 0:
        i1 += 1

    elif vect[i2] == 0 or i2 <= i1:
        i2 += 1

    else:
        # on a i1 < i2 et vect[i1] != 0 et vect[i2] != 0
        # on calcule le mouvement par lequel on va conjuguer M0
        M_txt = mvt_phase_2(i1 + 1, i2 + 1)
        Mi_txt = inverser(M_txt)

        # on multiplie enfin <configuration> par <M0> conjugé par <M>
        configuration *= executer(Mi_txt) * M0 * executer(M_txt)
        sol += Mi_txt + M0_txt + M_txt

print('Configuration après la phase 2 :')
print(configuration)

# PHASE 3 : placement des arêtes

M0, M0_txt = L * r * U ** 2 * l * R * B ** 2, 'LrUUlRBB' # Ce mouvement permute trois arêtes (selon un 3-cycle) et laisse tous les autres cubes inchangés

# Pour chaque trois-cycle qui compose la permutation sur les arêtes de la configuration, on calcule un mouvement qui l'inverse par conjugaison
for trois_cycle in configuration.perm_aretes.produit_trois_cycles:
    c1, c2, c3 = trois_cycle.representation_cycle[0], trois_cycle.representation_cycle[1], trois_cycle.representation_cycle[2]

    # Mouvement qui permet la conjugaison
    M_txt = mvt_phase_3(c3, c2, c1)
    Mi_txt = inverser(M_txt)

    # On multiplie <configuration> par <M0> conjugué par <M>
    configuration *= executer(Mi_txt) * M0 * executer(M_txt)
    sol += Mi_txt + M0_txt + M_txt

print('Configuration après la phase 3 :')
print(configuration)

# mvt_phase_3 = [[]]

# for i in range(13):
#     temp = []

#     for j in range(13):
#         temp.append([''] * 13)
    
#     mvt_phase_3.append(temp)

# mvts = ['', 'U', 'D', 'R', 'L', 'B', 'F', 'u', 'd', 'r', 'l', 'b', 'f']
# compteur = 0

# for i1 in range(13):
#     print(i1 * 1 / 13, '%')
#     for i2 in range(13):
#         for i3 in range(13):
#             for i4 in range(13):
#                 for i5 in range(13):
#                     for i6 in range(13):
#                         mot = mvts[i1] + mvts[i2] + mvts[i3] + mvts[i4] + mvts[i5] + mvts[i6]
#                         images_perm_aretes = executer(mot).perm_aretes.images

#                         c1, c2, c3 = images_perm_aretes[0], images_perm_aretes[2], images_perm_aretes[8]

#                         if mvt_phase_3[c1][c2][c3] == '':
#                             compteur += 1
#                             mvt_phase_3[c1][c2][c3] = mot

# print(mvt_phase_3)
# print("nombre de mots ajoutés : ", compteur)