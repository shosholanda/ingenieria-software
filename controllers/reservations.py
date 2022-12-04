from flask import Blueprint, render_template, request, session, redirect, url_for
from models.model_reservaciones import crear_reservacion as create
from models.model_usuarios import *
from alchemyClasses.reservacion import Reservacion

view_reservations = Blueprint('reservacion', __name__, url_prefix='/reservacion')

#localhost:5000/reservs/
@view_reservations.route("/", methods=['GET', 'POST'])
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
        return render_template("reservacion/show-reservations.html")
    return render_template("reservacion/reservations.html")


#Página de creacion de model_reservaciones
@view_reservations.route("/crear", methods=['GET', 'POST'])
def crear_reservacion():
    if request.method == 'POST':
        error = None
        mail = request.form['email']
        usr = obten_usuario(mail)
        if usr == None:
            #El usuario no existe y se puede crear
            hostal = 1 #request.form['hoteles']
            num_personas = request.form['num_personas']
            inicio = request.form['fecha_inicio']
            fin = request.form['fecha_salida']

            try:
                num_personas = int(num_personas)
            except:
                error = 'Ingrese un número válido'
                return redirect(url_for('reservacion.crear_reservacion'))
            resv = Reservacion(mail, hostal, num_personas, inicio, fin, 1)
            if create(resv) != None:
                error = "Hubo un error al registrar al indiviuo"
            #pasó las validaciones
            if error == None:
                #Crear usuario
                return redirect(url_for('login.success'))
            else:
                return error

        else:
            error = "El correo no está en la base de datos y no puede hacer una reservacion"
            return render_template("auth/failure.html")
    return render_template("reservacion/reservations.html")



