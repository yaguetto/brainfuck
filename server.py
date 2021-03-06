import interpretador
import json
import codecs
import multiprocessing
import time
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def serve_indice():
    return render_template("interface.html", a=" ")

@app.route("/", methods=["POST"])
def processa_brainfuck():
    codigo = request.form.getlist('codigo_input')
    codigo_string = str(codigo[0])
    buffer = HTTPBuffer()
    process_interpretar = multiprocessing.Process(target = interpretador.server, args=(codigo_string, buffer))
    process_interpretar.start()
    process_interpretar.join(timeout = 0.5)
    process_interpretar.terminate()
    if process_interpretar.is_alive():
        print(codigo_string, "=", "excedeu o tempo de execução")
        return render_template("interface.html", a="excedeu o tempo de execução")
    print(codigo_string, "=", buffer.buffer)
    return render_template("interface.html", a=buffer.buffer)

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
