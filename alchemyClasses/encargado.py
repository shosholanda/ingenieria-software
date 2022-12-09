from alchemyClasses.__init__ import db
from alchemyClasses.usuario import Usuario

class encargado(Usuario):

    #Encargado completo
    def __init__(self,  email,
                        nombre,
                        passwd,
                        edad,
                        celular,
                        nacionalidad,
                        tipo_usuario = 2,):
        self.email = email
        self.nombre = nombre
        self.passwd = passwd
        self.edad = edad
        self.celular = celular
        self.nacionalidad = nacionalidad
        self.tipo_usuario = tipo_usuario

    def __repr__(self) -> str:
        return f'Encargado: {self.nombre}\nCorreo: {self.email}\nContra: {self.passwd}'
