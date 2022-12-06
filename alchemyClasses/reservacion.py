from alchemyClasses.__init__ import db

class Reservacion(db.Model):

    __tablename__ = 'reservacion'
    idreservacion = db.Column("idreservacion", db.Integer, primary_key=True)
    correo = db.Column("correo", db.String(50))
    idhostal = db.Column("idhostal", db.Integer)
    num_personas = db.Column("numero_personas", db.Integer)
    inicio = db.Column("fecha_llegada", db.Date)
    final = db.Column("fecha_salida", db.Date)
    tipo_reservacion = db.Column("tipo_reservacion", db.Integer)

    def __init__(self,correo,
                        idhostal,
                        num_personas,
                        inicio,
                        final,
                        tipo_reservacion):
        self.correo = correo
        self.idhostal = idhostal
        self.num_personas = num_personas
        self.inicio = inicio
        self.final = final
        self.tipo_reservacion = tipo_reservacion

