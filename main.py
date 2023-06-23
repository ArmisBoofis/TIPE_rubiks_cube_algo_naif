from outils_permutations import Cycle, Permutation
from vecteurs_orientation import VecteurOrientation

perm1 = Permutation([2, 5, 9, 3, 7, 8, 6, 4, 1])
perm2 = Permutation([3, 6, 2, 4, 8, 1, 7, 5, 9])

cycle1 = Cycle((1, 3, 4, 5, 6), 9)

vect1 = VecteurOrientation([0, 1, 2, 2, 1, 0, 1, 0], 3)
vect2 = VecteurOrientation([0, 2, 1, 0, 1, 0, 2, 2], 3)

print(vect1, vect2)
print(vect1 + vect2)