import sys

def main():
    ler_arquivo(sys.argv[1])

def ler_arquivo(arquivo):
    arquivo_lido = open(arquivo, 'r')
    conteudo = arquivo_lido.read()
    arquivo_lido.close()
    return conteudo

if __name__ == '__main__':
    main()
