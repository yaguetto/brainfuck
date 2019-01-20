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
    return 'x'