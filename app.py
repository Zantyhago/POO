from flask import Flask
app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Mi primera aplicacion con Flask anashei /n'

if __name__ == '__main__':
    app.run()