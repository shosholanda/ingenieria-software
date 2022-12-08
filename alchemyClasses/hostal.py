from alchemyClasses.__init__ import db

class Hostal(db.Model):

    __tablename__ = 'hostal'
    idhostal = db.Column("idhostal", db.Integer, primary_key=True)
    nombre = db.Column("nombre", db.String(50))
    estado = db.Column("estado", db.String(50))
    idactividad = db.Column("idactividad", db.Integer)

    def __init__(self,
                 idhostal,
                 nombre,
                 estado,
                 idactividad):
        self.idhostal = idhostal
        self.nombre = nombre
        self.estado = estado
        self.idactividad = idactividad

