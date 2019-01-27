import interpretador
import codecs
from flask import Flask, render_template, request
app = Flask(__name__)

abrir_arquivo = codecs.open("interface.html", "r", "UTF-8")
index = abrir_arquivo.read()
abrir_arquivo.close()


@app.route("/")
def serve_index():
    return index

@app.route("/", methods=["POST"])
def processa_brainfuck():
    codigo = request.form.getlist('codigo_input')
    codigo_string = str(codigo[0])
    print(codigo_string)
    buffer = HTTPBuffer()
    interpretador.server(codigo_string, buffer)
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
