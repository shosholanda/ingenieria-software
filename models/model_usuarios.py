from alchemyClasses.usuario import Usuario
from alchemyClasses.__init__ import db

def obten_usuario(email_arg):
    ans = Usuario.query.filter(Usuario.email == email_arg).first()
    return ans

def valida_usuario(correo, contra):
    ans = Usuario.query.filter(Usuario.email == correo,Usuario.passwd == contra).first()
    return ans

def valida_contraseña(contra):
    ans = Usuario.query.filter(Usuario.passwd == contra).first()
    return ans

def valida_correo(correo):
    ans = Usuario.query.filter(Usuario.email == correo).first()
    return ans

#Crea un usuario
def crear_usuario(usuario):
    db.session.add(usuario)
    db.session.commit()
