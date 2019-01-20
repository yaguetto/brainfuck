import interpretador
from flask import Flask
app = Flask(__name__)

index = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Brainfuck interpreter</title>
    <h1>Brainfuck interpreter</h1>
    <p>Interpretador de Brainfuck desenvolvido por Gustavo Kawamoto e Yago Rogatto.</p>
</head>
<body>
    <form action="/" method="POST">
        <div>
            <label for="code">Código:</label>
            <br>
                <textarea name="code"></textarea>
        </div>
            <input type="submit">
    </form>

    <dl>
        <dt>GitHub Gustavo:</dt>
        <dd><li><a href = "https://github.com/gkawamoto">Gkawamoto</a></li></dd>
        <dt>GitHub Yago:</dt>
        <dd><li><a href = "https://github.com/yaguetto">Yaguetto</a></li></d>
    </dl>
</body>
</html>>
'''

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
    return ''

class HTTPBuffer:
    # escreve no buffer do terminal
    def write(self, text):
        print(text)
    # renderiza o que esta escrito no buffer e esvazia
    def flush(self):
        pass
    # lendo a proxima tecla e retornando ela
    def read(self, size):
        return ''
