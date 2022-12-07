
from alchemyClasses.usuario import Usuario

def obten_usuario(email_arg):
    ans = Usuario.query.filter(Usuario.email == email_arg).first()
    return ans

def valida_usuario(correo, contra):
    ans = Usuario.query.filter(Usuario.email == correo,Usuario.passwd == contra).first()
    return ans
