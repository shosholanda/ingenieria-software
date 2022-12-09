from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models.model_reservaciones import crear_reservacion as create
from models.model_reservaciones import obtener_reservacion
from models.model_reservaciones import obtener_reservaciones
from models.model_reservaciones import elimina_reservacion as elim_resv
from models.model_usuarios import *
from alchemyClasses.reservacion import Reservacion
from controllers.login import login_required
from models.model_hostales import obtener_hostal
from models.model_hostales import obtener_hostales

import itertools


view_encargados = Blueprint('usuarios', __name__, url_prefix='/usuarios')

'''Controlador de reservaciones.
Aquí se reciben los datos de entrada, se hacen las validaciones y se manda llamar a las consultas del modelo'''


#localhost:5000/reservs/
@view_encargados.route("/", methods=['GET', 'POST'])
@login_required
def reservations_main_page():
    #Codigo python.
    if request.method == 'POST':
        error = None
        mail = request.form['email']
        reservacion = obtener_reservaciones(mail)
        if reservacion != None:
            session['reservation'] = True
        else:
            session['reservation'] = False
        return render_template("index.html")
    return render_template("auth/success.html")


#CREATE model_reservaciones
@view_reservations.route("/crear", methods=['GET', 'POST'])
@login_required
def crear_reservacion():
    hostales_disponibles = obtener_hostales()
    if request.method == 'POST':
        error = None
        #El usuario existe y se pueden agregar reservaciones
        try:
            idhostal = request.form['hotel']
            num_personas = request.form['num_personas']
            inicio = request.form['fecha_inicio']
            fin = request.form['fecha_salida']

            num_personas = int(num_personas)
            hostal = obtener_hostal(idhostal).nombre
            resv = Reservacion(session['mail'], idhostal, num_personas, inicio, fin, hostal)
            create(resv)
        except:
            error = 'Datos incorrectos'
            flash(error)
            return redirect(url_for('reservacion.crear_reservacion'))

        #pasó las validaciones
        if error == None:
            #Crear usuario
            return redirect(url_for('login.success'))
        else:
            flash(error)
            return f"<h1> {error} </h1>"

    return render_template("reservacion/reservations.html", hostales = hostales_disponibles)

#READ reservacion
@view_reservations.route("/consultar", methods=['GET'])
@login_required
def consultar_reservaciones():
    resultados = obtener_reservaciones(session['mail'])
    resultados = reversed(list(resultados))
    if not resultados:
        return "<p>No se encontraron reservaciones para este usuario</p>"
    return render_template("reservacion/show-reservations.html", consulta = resultados)

#UPDATE reservacion
@view_reservations.route("/actualizar/<int:idresv>", methods=['GET', 'POST'])
@login_required
def actualiza_reservacion(idresv):
    hostales_disponibles = obtener_hostales()
    if request.method == 'POST':
        error = None

        resv_old = obtener_reservacion(idresv)
        #El usuario existe y se pueden agregar reservaciones
        try:
            resv_old.num_personas = int(request.form['num_personas'])
        except:
            error = 'Datos incorrectos'
            flash(error)
            return redirect(url_for('reservacion.actualiza_reservacion', idresv=idresv))
        resv_old.idhostal = request.form['hotel']
        resv_old.inicio = request.form['fecha_inicio']
        resv_old.fin = request.form['fecha_salida']
        if resv_old.idhostal == '' or resv_old.inicio == '' or resv_old.fin == '':
            error = 'Por favor llena todos los campos'
        else:
            hostal = obtener_hostal(resv_old.idhostal).nombre
            resv_old.hostal = hostal
            create(resv_old)
        #pasó las validaciones
        if error == None:
            #Crear usuario
            return redirect(url_for('login.success'))
        else:
            flash(error)
            return redirect(url_for('reservacion.actualiza_reservacion', idresv=idresv))
    return render_template("reservacion/update_reservation.html", hostales = hostales_disponibles)

@view_reservations.route("/delete/<int:idresv>", methods=['GET', 'POST'])
@login_required
def elimina_reservacion(idresv):
    resv = obtener_reservacion(idresv)
    elim_resv(resv)
    return redirect(url_for("reservacion.consultar_reservaciones"))


