# lista é definido por []

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista)
print(lista_animal[1])

for x in lista_animal:
    print(x)

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

# soma
print(sum(lista))

# maior valor
print(max(lista))

# menor valor (no caso é o cachorro pois o 'C' é a primeira letra alfabética
print(min(lista_animal))

