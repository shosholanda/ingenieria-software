from alchemyClasses.reservacion import Reservacion
from alchemyClasses.usuario import Usuario
from alchemyClasses.__init__ import db

#Aquí estan todas las consultas a la base de datos

#Obtiene una reservacion
def obtener_reservacion(idreservacion):
    ans = Reservacion.query.filter(Reservacion.idreservacion == idreservacion).first()
    return ans

#Obtiene todas las reservaciones de la persona
def obtener_reservaciones(email):
    return Reservacion.query.filter(Reservacion.correo == email)

#Crea una reservacion. También sirve para actualizar
def crear_reservacion(reservacion):
    db.session.add(reservacion)
    db.session.commit()

#Elimina una reservacion
def elimina_reservacion(reservacion):
    db.session.delete(reservacion)
    db.session.commit()
