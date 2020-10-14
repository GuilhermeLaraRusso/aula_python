# Módulo são arquivos.py

# Importação de outros módulos

from aula7_4 import Televisao
from aula7_2 import Calculadora
from aula8_2 import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra de lista: {}'.format(total_letras))
