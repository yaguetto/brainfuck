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
    return caractere != '>' and caractere != '<' and caractere != '+' and caractere != '-' and caractere != ',' and caractere != '.' and caractere != '[' and caractere != ']' and caractere != ';'

def criar_memoria():
    memoria = []
    for i in range(0,30000):
        memoria.append(0)
    return memoria

def interpretar(codigo):
    memoria = criar_memoria()
    ponteiro = 0
    controle_loop = []
    indice_caractere = 0
    while indice_caractere < len(codigo):
        caractere = codigo[indice_caractere]
        if verificar_caractere_invalido(caractere):
            indice_caractere = indice_caractere + 1
            continue
        #print(indice_caractere, caractere)
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
            sys.stdout.flush()
        if caractere == ';':
            print(memoria[ponteiro])
        if caractere == '[':
            if memoria[ponteiro] != 0:
                controle_loop.append(indice_caractere)
            if memoria[ponteiro] == 0:
                contador_loop = 1
                while contador_loop != 0:
                    indice_caractere += 1
                    if codigo[indice_caractere] == '[':
                        contador_loop += 1
                    if codigo[indice_caractere] == ']':
                        contador_loop -= 1
                #print(indice_caractere, ']')
                #indice_caractere += 1
        if caractere == ']':
            x = controle_loop.pop()
            indice_caractere = x
        if caractere == ',':
            proxima_tecla = sys.stdin.read(1)
            if len(proxima_tecla) == 0:
                memoria[ponteiro] = 0
            else:
                memoria[ponteiro] = ord(proxima_tecla)
        if caractere != ']':
            indice_caractere = indice_caractere + 1
    print()

if __name__ == '__main__':
    main()