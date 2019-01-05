import sys

def main():
    codigo = ler_arquivo(sys.argv[1])
    interpretar(codigo)

def ler_arquivo(arquivo):
    arquivo_lido = open(arquivo, 'r')
    conteudo = arquivo_lido.read()
    arquivo_lido.close()
    return conteudo

def verificar_caractere_invalido(caractere):
    return caractere != '>' and caractere != '<' and caractere != '+' and caractere != '-' and caractere != ',' and caractere != '.' and caractere != '[' and caractere != ']'

def criar_memoria():
    memoria = []
    for i in range(0,30000):
        memoria.append(0)
    return memoria

def interpretar(codigo):
    memoria = criar_memoria()
    ponteiro = 0
    indice_caractere = 0
    stack_controle = []
    while indice_caractere < len(codigo):
        caractere = codigo[indice_caractere]
        if verificar_caractere_invalido(caractere):
            indice_caractere = indice_caractere + 1
            continue
        if caractere == '>':
            ponteiro = (ponteiro + 1) % len(memoria)
        if caractere == '<':
            ponteiro = (ponteiro - 1) % len(memoria)
        if caractere == '+':
            memoria[ponteiro] = (memoria[ponteiro] + 1) % 256
        if caractere == '-':
            memoria[ponteiro] = (memoria[ponteiro] - 1) % 256
        if caractere == '.':
            sys.stdout.write(chr(memoria[ponteiro]))
        indice_caractere = indice_caractere + 1
    print()

if __name__ == '__main__':
    main()
