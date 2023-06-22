from outils_permutations import Cycle, Permutation

perm1 = Permutation([2, 5, 9, 3, 7, 8, 6, 4, 1])
perm2 = Permutation([3, 6, 2, 4, 8, 1, 7, 5, 9])

cycle1 = Cycle((1, 3, 4, 5, 6), 9)

print(cycle1.images)

cycle1.images = ((1, 4, 6), 6)

print(cycle1.images)