from alchemyClasses.__init__ import db

class Reservacion(db.Model):

    __tablename__ = 'reservacion'
    idreservacion = db.Column("idreservacion", db.Integer, primary_key=True)
    inicio = db.Column("fecha_llegada", db.Date)
    final = db.Column("fecha_salida", db.Date)
    idusuario = db.Column("correo", db.String(200), db.ForeignKey('usuarios.email'), nullable = False)

    def __init__(self, idreservacion, inicio, final, idusuario):
        self.idreservacion = idreservacion
        self.inicio = inicio
        self.final = final
        self.idusuario = idusuario

