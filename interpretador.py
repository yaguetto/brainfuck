import sys

def main():
    codigo = ler_arquivo(sys.argv[1])
    codigo = otimizar_codigo(codigo)
    buffer = ConsoleBuffer()
    interpretar(codigo, buffer)

def ler_arquivo(arquivo):
    arquivo_lido = open(arquivo, 'r')
    conteudo = arquivo_lido.read()
    arquivo_lido.close()
    return conteudo

def otimizar_codigo(codigo):
    colchete_aberto = 0
    colchete_fechado = 0
    controle_colchete = []
    resultado_codigo = []
    for letra in codigo:
        if verificar_caractere_invalido(letra):
            continue
        if letra == '[':
            colchete_aberto = colchete_aberto + 1
            controle_colchete.append(letra)
        elif letra == ']':
            colchete_fechado = colchete_fechado + 1
            try:
                if controle_colchete[-1] == '[':
                    controle_colchete.append(letra)
                else:
                    return "Colchete fechado a mais."
            except:
                return "Colchete fechado a mais."
        resultado_codigo.append(letra)
    if colchete_aberto != colchete_fechado:
        if colchete_aberto > colchete_fechado:
            return "Colchete aberto a mais."
        else:
            return "Colchete fechado a mais."
    return resultado_codigo

def verificar_caractere_invalido(caractere):
    return caractere != '>' and caractere != '<' and caractere != '+' and caractere != '-' and caractere != ',' and caractere != '.' and caractere != '[' and caractere != ']' and caractere != ';'

def criar_memoria():
    memoria = []
    for i in range(0,30000):
        memoria.append(0)
    return memoria

def interpretar(codigo, buffer):
    memoria = criar_memoria()
    ponteiro = 0
    controle_loop = []
    indice_caractere = 0
    while indice_caractere < len(codigo):
        caractere = codigo[indice_caractere]
        if caractere == '>':
            ponteiro = (ponteiro + 1) % 30000
        elif caractere == '<':
            ponteiro = (ponteiro - 1) % 30000
        elif caractere == '+':
            memoria[ponteiro] = (memoria[ponteiro] + 1) % 256
        elif caractere == '-':
            memoria[ponteiro] = (memoria[ponteiro] - 1) % 256
        elif caractere == '.':
            buffer.write(chr(memoria[ponteiro]))
            buffer.flush()
        elif caractere == ';':
            print(memoria[ponteiro])
        elif caractere == '[':
            if memoria[ponteiro] != 0:
                controle_loop.append(indice_caractere)
            elif memoria[ponteiro] == 0:
                contador_loop = 1
                while contador_loop != 0:
                    indice_caractere += 1
                    if codigo[indice_caractere] == '[':
                        contador_loop += 1
                    elif codigo[indice_caractere] == ']':
                        contador_loop -= 1
        elif caractere == ']':
            x = controle_loop.pop()
            indice_caractere = x
        elif caractere == ',':
            proxima_tecla = buffer.read(1)
            if len(proxima_tecla) == 0:
                memoria[ponteiro] = 0
            else:
                memoria[ponteiro] = ord(proxima_tecla)
        if caractere != ']':
            indice_caractere = indice_caractere + 1

def server(codigo, buffer):
    codigo_otimizado = otimizar_codigo(codigo)  
    if codigo_otimizado == "Colchete aberto a mais." or codigo_otimizado == "Colchete fechado a mais.":
        buffer.buffer = codigo_otimizado
        return
    interpretar(codigo_otimizado, buffer)
    return

class ConsoleBuffer:
    # escreve no buffer do terminal
    def write(self, text):
        sys.stdout.write(text)
    # renderiza o que esta escrito no buffer e esvazia
    def flush(self):
        sys.stdout.flush()
    # lendo a proxima tecla e retornando ela
    def read(self, size):
        return sys.stdin.read(size)
        

if __name__ == '__main__':
    main()