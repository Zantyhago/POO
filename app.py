from flask import Flask
app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Mi primera aplicacion con Flask anashe'

@app.route('/saludo_bienvenida')
def saludoBienvenida():
 return 'Bienvenido a mi aplicación'

@app.route('/saludo_despedida')
def saludoDespedida():
 return 'Gracias por visitar mi aplicación Flask'

if __name__ == '__main__':
    app.run()