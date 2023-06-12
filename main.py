from outils_permutations import Permutation

perm1 = Permutation([2, 5, 9, 3, 7, 8, 6, 4, 1])
perm2 = Permutation([3, 6, 2, 4, 8, 1, 7, 5, 9])

for cycle in perm2.produit_cycles:
    print(cycle)
    print()