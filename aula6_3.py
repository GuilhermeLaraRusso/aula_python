conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

# '.issubset' serve para saber se um conjunto é subconjunto de outro
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))

conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}'.format(conjunto_subset2))

# .issuperset serve para saber se um conjunto é superconjunto de outro
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}'.format(conjunto_superset))
