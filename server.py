import interpretador
import json
import codecs
from flask import Flask, render_template, request
app = Flask(__name__)

arquivo_aberto = codecs.open("interface.html", "r", "UTF-8")
indice = arquivo_aberto.read().replace("'codigo aqui'", " ")
arquivo_aberto.close()


@app.route("/")
def serve_indice():
    return indice

@app.route("/", methods=["POST"])
def processa_brainfuck():
    codigo = request.form.getlist('codigo_input')
    codigo_string = str(codigo[0])
    buffer = HTTPBuffer()
    interpretador.server(codigo_string, buffer)
    print(codigo_string, "=", buffer.buffer)
    arquivo_aberto = codecs.open("interface.html", "r", "UTF-8")
    indice = arquivo_aberto.read().replace("'codigo aqui'", json.dumps(buffer.buffer))
    arquivo_aberto.close()
    return indice

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
