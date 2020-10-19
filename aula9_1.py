
# open ('w') serve para escrever e sobrescrever o arquivo. se já existe o arquivo, ele irá escrever
# open ('a') serve para continuar a escrever no arquivo.

# arquivo = open('teste.txt', 'w')
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nTerceira linha')
# arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    # escrever_arquivo('Primeira linha.\n')
    # atualizar_arquivo('Terceira linha.\n')
    ler_arquivo('teste.txt')