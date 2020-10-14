lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('não existe um gato na lista')

if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista, será incluido')
    lista_animal.append('lobo')
    print(lista_animal)
# append é uma função da lista e adiciona um item

lista_animal.pop()
print(lista_animal)
# .pop retira a última posição da lista (ou o valor indicado)

lista_animal.remove('elefante')
print(lista_animal)
# .remove remove um elemento já conhecido pelo nome

