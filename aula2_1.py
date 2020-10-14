a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))

# {}: concatena qualquer tipo. Pode ser string, inteiro, variavel, etc...
print('soma: {}' .format(soma))
# str: transforma em string
print('soma: ' + str(soma))
print('subtração: ' + str(subtracao))
print(multiplicacao)

# int: transforma em inteiro
print(divisao)
print(type(divisao))
print(int(divisao))
print(resto)


print('Soma: {alias1} \nSubtração: {alias2} '
      '\nMultiplicação: {alias3} '
      '\nDivisão: {alias4} '
      '\nResto: {alias5}'
      .format(alias1=soma,
              alias2=subtracao,
              alias3=multiplicacao,
              alias4=divisao,
              alias5=resto))



# x = '5'
# soma2 = int(x) + 1
# print(soma2)

