from alchemyClasses.reservacion import Reservacion
from alchemyClasses.usuario import Usuario
from alchemyClasses.__init__ import db

#Aquí estan todas las consultas a la base de datos

#Obtiene una reservacion
def obtener_reservacion(email):
    ans = Reservacion.query.filter(Reservacion.correo == email).first()
    return ans

#Obtiene todas las reservaciones de la persona
def obtener_reservaciones(email):
    return Reservacion.query.filter(Reservacion.correo == email)

#Crea una reservacion
def crear_reservacion(reservacion):
    db.session.add(reservacion)
    db.session.commit()
