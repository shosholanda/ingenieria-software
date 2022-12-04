from alchemyClasses.reservacion import Reservacion
from alchemyClasses.usuario import Usuario
from alchemyClasses.__init__ import db


#Obtiene una reservacion
def obtener_reservacion(email):
    ans = Reservacion.query.filter(Reservacion.correo == email).first()
    return ans

#Obtiene todas las reservaciones de la persona
def obtener_reservaciones(email):
    return Reservacion.query.filter(Reservacion.correo == email)

#Crea una reservacion
def crear_reservacion(reservacion):
    user = Usuario.query.filter(Usuario.email == reservacion.correo).first()
    if not user:
        #se procede a crear la tabla
        db.session.add(reservacion)
        db.session.commit()
    else:
        #No se puede añadir el usuario
        return "El correo no está en la base de datos y no puede hacer una reservacion"
