from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Sucursal as sucursal, Repartidor as repartidor, Paquete as paquete, Transporte as transporte
import datetime

app = Flask(__name__)

app.config.from_object('config')
db.init_app(app)

@app.route('/', methods = ['GET', 'POST'])          # 1. Acceso del despachante a la app
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

def generaNumEnvio():       # 2. Registrar la recepcion de un paquete
    PaqueteFinal = paquete.query.order_by(paquete.numeroenvio.desc()).first()
    if PaqueteFinal:
        print(f'Numero del ultimo paquete registrado: {PaqueteFinal.numeroenvio} - Del nuevo: {nuevoNumeroPack}')
        ultimoNumero = int(PaqueteFinal.numeroenvio)
        nuevoNumeroPack = ultimoNumero + 20
    else:
        nuevoNumeroPack = 1000
    return nuevoNumeroPack

@app.route('/GuardarPaquete/<int:idSucursal>', methods=['GET', 'POST'])
def GuardarPaquete(idSucursal):
    Sucursal = sucursal.query.get_or_404(idSucursal)    
    if request.method == 'POST':
        try:
            xpaquete = paquete(
                numeroenvio = generaNumEnvio(),
                peso = request.form['peso'],
                nomdestinatario = request.form['nomdestinatario'], 
                dirdestinatario = request.form['dirdestinatario'],  
                idsucursal = idSucursal,
                entregado = False)
            db.session.add(xpaquete)
            db.session.commit()
            flash(f'Se registró exitosamente el paquete en la sucursal {idSucursal}')
            return redirect(url_for('gestorDespachos', idSucursal = idSucursal))
        except ValueError as e:
            db.session.rollback()
            flash(f'{e} Valor ingresado erroneo.', 'error')
        except Exception as e:
            db.session.rollback()
            flash(f'{e} Se produjo un error al registrar el paquete.', 'error')
    return render_template('GuardarPaquete.html', sucursal = Sucursal)

def generaNumTrans():
    TransFinal = transporte.query.order_by(transporte.numerotransporte.desc()).first()
    if TransFinal:
        ultimoNumero = int(TransFinal.numerotransporte)
        nuevoNumero = ultimoNumero + 1
        print(f"Numero del ultimo transporte registrado: {ultimoNumero} - Del nuevo: {nuevoNumero}")
    else:
        nuevoNumero = 1000
    return nuevoNumero

@app.route('/nuevaSalida/<int:idSucursal>', methods=['GET', 'POST'])
def nuevaSalida():
    Sucursal = sucursal.query.get_or_404(idSucursal)
    sucursalActual = str(Sucursal).split()
    sucursalActual = sucursalActual[-1].replace(">", "")
    print(f'Sucursal actual: {sucursalActual}')
    if request.method == 'POST':
        idSucursal = request.form.get('sucursal_destino')
        print(f" la sucursal destino es {idSucursal}")
        paquetesSeleccionados = request.form.getlist('paquetes')
        if idSucursal and paquetesSeleccionados:
            try:
                xtransporte = transporte(
                    numerotransporte = generaNumTrans(),
                    fyhSalida = datetime.now(),
                    idsucursal = idSucursal,)
                db.session.add(xtransporte)
                for paqueteId in paquetesSeleccionados:
                    Paquete = paquete.query.get(paqueteId)
                    Paquete.idtransporte = xtransporte.id
                db.session.commit()
                flash('Salida de transporte registrada', 'success')
            except Exception as e:
                db.session.rollback()
                flash(f'Error al registrar el transporte: {e}', 'error')
        else:
            if not idSucursal:
                flash('Seleccione una sucursal de destino', 'warning')
            if not paquetesSeleccionados:
                flash('Seleccione al menos un paquete para el transporte', 'warning')
        return redirect(url_for('panelDespachante', idSucursal=sucursalActual))
    
    sucursales = Sucursal.query.filter(Sucursal.id != sucursalActual).order_by(Sucursal.numero).all()
    paquetes = Paquete.query.filter_by(idsucursal=sucursalActual, entregado=False, idrepartidor=None, idtransporte=None).all()
    
    return render_template('registrar_salida.html', sucursal=sucursal, sucursales=sucursales, paquetes=paquetes)