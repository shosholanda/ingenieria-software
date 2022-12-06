from flask import Blueprint, render_template, request, session, redirect, url_for
from models.model_reservaciones import crear_reservacion as create
from models.model_reservaciones import obtener_reservacion
from models.model_reservaciones import obtener_reservaciones
from models.model_usuarios import *
from alchemyClasses.reservacion import Reservacion

view_reservations = Blueprint('reservacion', __name__, url_prefix='/reservacion')

'''Controlador de reservaciones.
Aquí se reciben los datos de entrada, se hacen las validaciones y se manda llamar a las consultas del modelo'''


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
        return render_template("index.html")
    return render_template("auth/success.html")


#Página de creacion de model_reservaciones
@view_reservations.route("/crear", methods=['GET', 'POST'])
def crear_reservacion():
    if request.method == 'POST':
        error = None
        usr = obten_usuario(session['mail'])
        print(usr)
        if usr != None:
            #El usuario existe y se pueden agregar reservaciones
            hostal = 1 #request.form['hoteles']
            num_personas = request.form['num_personas']
            inicio = request.form['fecha_inicio']
            fin = request.form['fecha_salida']

            try:
                num_personas = int(num_personas)
            except:
                error = 'Ingrese un número válido'""
                return f"<h1> {error} </h1>"
            resv = Reservacion(session['mail'], hostal, num_personas, inicio, fin, 1)
            create(resv)
            #pasó las validaciones
            if error == None:
                #Crear usuario
                return redirect(url_for('login.success'))
            else:
                return f"<h1> {error} </h1>"

        else:
            error = "El correo no está en la base de datos y no puede hacer una reservacion"
            return f"<h1> {error} </h1>"
    return render_template("reservacion/reservations.html")

@view_reservations.route("/consultar", methods=['GET'])
def consultar_reservacion():
    resultados = obtener_reservacion(session['mail'])
    print(resultados)
    if not resultados:
        return "<p>No se encontraron reservaciones para este usuario</p>"
    session['reservations'] = resultados
    return render_template("reservacion/show-reservations.html")

@view_reservations.route("/consultar", methods=['GET'])
def consultar_reservaciones():
    resultados = obtener_reservaciones(session['mail'])
    print(type(resultados))
    s = ""
    if not resultados:
        return "<p>No se encontraron reservaciones para este usuario</p>"
    return render_template("reservacion/show-reservations.html")




