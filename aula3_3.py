a = int(input('Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))
else:
    print('Foi informado alguma nota errada')