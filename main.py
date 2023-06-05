from outils_permutations import Permutation

perm1 = Permutation([2, 5, 9, 3, 7, 8, 6, 4, 1])
perm2 = Permutation([3, 6, 2, 4, 8, 1, 7, 5, 9])

print(perm1 * perm1.inverse())