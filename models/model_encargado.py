from alchemyClasses.encargado import encargado
from alchemyClasses.usuario import Usuario
from alchemyClasses.__init__ import db

#Aquí estan todas las consultas a la base de datos

#Obtiene todas los encargados
def obtener_encargados(email):
    return encargado.query.filter(encargado.email == email)

#Crea un encargado. También sirve para actualizar
def crear_encargado(encargado):
    db.session.add(encargado)
    db.session.commit()

#Elimina una encargado
def elimina_encargado(encargado):
    db.session.delete(encargado)
    db.session.commit()
