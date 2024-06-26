from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Sucursal as sucursal, Repartidor as repartidor, Paquete as paquete, Transporte as trasnsporte
import datetime

app = Flask(__name__)

app.config.from_object('config')
db.init_app(app)

@app.route('/', methods = ['GET', 'POST'])          # 1. Acceso a la app como despachante
def access():
    if request.method == 'POST':
        xidSucursal = request.form.get('Sucursal')
        if xidSucursal:
            idSucursal = xidSucursal
            return redirect(url_for('gestorDespachos', idSucursal))
    listasucursales = sucursal.query.order_by(sucursal.numero).all()    # guarda todas las sucursales de la db ordenadas por numero
    print(f"Se cargaron {len(listasucursales)} sucursales.")        # para verificar que se cargaron correctamente
    return render_template('sucursales.html', sucursales = listasucursales) # sucursales.html = despachantes

@app.route('/sucursal/<int:idSucursal>')
def gestorDespachos(idSucursal):
    xsucursal = sucursal.query.get_or_404(idSucursal)   # busca en la db la sucursal, si no está devuelve un error 404
    sucursal = xsucursal
    return render_template('gestorDespachante.html', sucursal)