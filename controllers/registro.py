from flask import Blueprint, render_template, request, redirect, url_for, flash, Markup
from models.model_usuarios import crear_usuario as create
from models.model_usuarios import *
from werkzeug.security import check_password_hash, generate_password_hash #This is only if security is enabled.
from alchemyClasses.usuario import Usuario
import hashlib
import re

registro = Blueprint('registro', __name__, url_prefix='/registro')

#Página de creacion de registro
@registro.route("/", methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':    
        try:
            error = None
            correo = request.form['correo']
            nombre = request.form['nombre']
            hash_contraseña = request.form['hash_contraseña']
            hash_contraseña = hashlib.sha256(hash_contraseña.encode('utf-8')).hexdigest()
            edad = request.form['edad']
            edad = int(edad)
            celular = request.form['celular']
            nacionalidad = request.form['nacionalidad']
            if re.search("admin.check.in", str(request.form['correo'])) != None:
                tipo_usuario = 0
            else: tipo_usuario = 1
            idactividades = 0
        except:
            error = Markup("<div><img class='P7' src='../static/f5.png' alt='Fondo-blanc'></div><div id='modal'>‎ <br>‎ <br>Por favor rellena todos los campos<a class='close 'href=''>&times;</a></div>")
            flash(error)
            return redirect(url_for('registro.crear_usuario'))
        if obten_usuario(correo) == None:
            usuario = Usuario(correo, nombre, hash_contraseña, edad, celular, nacionalidad, tipo_usuario, idactividades)
            create(usuario)

            if error == None:
            #Crear usuario
                exito = Markup("<div><img class='P7' src='../static/f5.png' alt='Fondo-blanc'></div><div id='modal'>‎ <br>‎ <br>Usuario registrado con exito! <a class='close 'href=''>&times;</a></div>")
                flash(exito)
                return redirect(url_for('registro.crear_usuario'))
            else:
                flash(error)
                return f"<h1> {error} </h1>"      
        else:
            existente = Markup("<div><img class='P7' src='../static/f5.png' alt='Fondo-blanc'></div><div id='modal'>‎ <br>‎ <br>Ya existe un usuario con ese correo <a class='close 'href=''>&times;</a></div>")
            flash(existente)
            return redirect(url_for('registro.crear_usuario'))

    
        
    return render_template("registro.html")


