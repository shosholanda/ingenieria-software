from alchemyClasses.hostal import Hostal
from alchemyClasses.__init__ import db

#Aquí estan todas las consultas a la base de datos

#Obtiene una reservacion
def obtener_hostal(idhostal):
    ans = Hostal.query.filter(Hostal.idhostal == idhostal).first()
    return ans


def obtener_hostales():
    return Hostal.query.all()
