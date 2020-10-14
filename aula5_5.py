# tupla é imutável, enquanto a lista é mutável.
# tupla é definido por ()

lista = [1, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla)
# tupla[0] = 12             não funciona pois a tupla não pode ser alterada

print(len(tupla))
print(len(lista_animal))

# converter lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)