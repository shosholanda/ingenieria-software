import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash #This is only if security is enabled.
from alchemyClasses.usuario import Usuario
from models.model_usuarios import obten_usuario, valida_usuario
import hashlib

loginBlueprint = Blueprint('login', __name__, url_prefix='/login')

@loginBlueprint.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['username']
        passwd = request.form['password']
        passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
        mail = request.form['email']
        usuario = Usuario(mail, nombre, passwd)
        if valida_usuario(mail, passwd, nombre) != None: #El usuario existe.
            #return render_template("success.html")
            session.clear()
            session['user_id'] = nombre
            session['mail'] = mail
            g.user = usuario.nombre
            return redirect(url_for("login.success"))
        else:
            return redirect(url_for("login.failure"))
    else: #Estamos haciendo un wget localhost:5000/login/
        return render_template('auth/login.html')

@loginBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('user_id') != None:
        return render_template("auth/success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('login.login'))

@loginBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("auth/failure.html")


@loginBlueprint.before_app_request
def load_logged_in_user():
    user_id = session.get('mail')
    print(user_id)
    if user_id is None:
        g.user = None
    else:
        g.user = Usuario.query.get_or_404(user_id)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login.login'))
        return view(**kwargs)
    return wrapped_view

