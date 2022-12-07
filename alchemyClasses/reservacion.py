from alchemyClasses.__init__ import db

class Reservacion(db.Model):

    __tablename__ = 'reservacion'
    idreservacion = db.Column("idreservacion", db.Integer, primary_key=True)
    correo = db.Column("correo", db.String(50))
    idhostal = db.Column("idhostal", db.Integer)
    num_personas = db.Column("numero_personas", db.Integer)
    inicio = db.Column("fecha_llegada", db.Date)
    final = db.Column("fecha_salida", db.Date)
    hostal = db.Column("hostal", db.String(50))

    def __init__(self,correo,
                        idhostal,
                        num_personas,
                        inicio,
                        final,
                        hostal):
        self.correo = correo
        self.idhostal = idhostal
        self.num_personas = num_personas
        self.inicio = inicio
        self.final = final
        self.hostal = hostal


    def __repr__(self):
        return f"Hostal:    {self.idhostal}\nNum. Personas:  {self.num_personas}\nFecha inicio:   {self.inicio}\nFinal:    {self.final}"
