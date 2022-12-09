from alchemyClasses.__init__ import db

class Usuario(db.Model):

    __tablename__ = 'usuario'
    email = db.Column('correo', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(200))
    passwd = db.Column('hash_contraseña', db.String(40))
    edad = db.Column('edad', db.Integer)
    celular = db.Column('celular', db.Integer)
    nacionalidad = db.Column('nacionalidad', db.String(50))
    tipo_usuario = db.Column('tipo_usuario', db.Integer)
    idactividades = db.Column('idactividad', db.Integer)

    #Usuario completo
    def init(self,  email,
                        nombre,
                        passwd,
                        edad,
                        celular,
                        nacionalidad,
                        tipo_usuario,
                        idactividades):
        self.email = email
        self.nombre = nombre
        self.passwd = passwd
        self.edad = edad
        self.celular = celular
        self.nacionalidad = nacionalidad
        self.tipo_usuario = tipo_usuario
        self.idactividades = idactividades

    def __repr__(self) -> str:
        return f'Usuario: {self.nombre}\nCorreo: {self.email}\nContra: {self.passwd}'
