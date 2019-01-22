import interpretador
import codecs
from flask import Flask
app = Flask(__name__)


abrir_html = codecs.open("interface.html", 'r', 'utf-8')
index = abrir_html.read()
abrir_html.close()

@app.route("/")
def serve_index():
    return index

@app.route("/", methods=["POST"])
def processa_brainfuck():
    codigo = '''
    +++++ +++++ [         Inicia as células com os valores:
  > +++++ +++         80
  > +++++ +++++ +     110
  > +++++ +++++       100
  > +++               30
  > +++++ +++         80
  > +++++ +++++ ++    120
  > +++++ +++++ +     110
  > +++++ +++++       100
  > +++++ +++++ +     110
  > +++               30
  <<<<<<<<<< -
]
> - .                 Imprime 'O'
> -- .                Imprime 'l'
> --- .               Imprime 'a'
> ++ .                Imprime '  '
> --- .               Imprime 'M'
> --- .               Imprime 'u'
> .                   Imprime 'n'
> .                   Imprime 'd'
> + .                 Imprime 'o'
> +++ .               Imprime '!'
,                     Espera uma tecla ser pressionada

    '''
    buffer = HTTPBuffer()
    interpretador.server(codigo, buffer)
    return buffer.buffer

class HTTPBuffer:
    def __init__(self):
        self.buffer = ''
    # escreve no buffer do terminal
    def write(self, text):
        self.buffer =  self.buffer + text
    # renderiza o que esta escrito no buffer e esvazia
    def flush(self):
        pass
    # lendo a proxima tecla e retornando ela
    def read(self, size):
        return ''
