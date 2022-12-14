from flask import Flask, redirect, url_for, render_template
from alchemyClasses.usuario import db
from controllers.auth import bp
from controllers.login import loginBlueprint
from controllers.logout import logoutBlueprint
from controllers.reservations import view_reservations
from controllers.registro import registro
import templates

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(bp)
app.register_blueprint(loginBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(view_reservations)
app.register_blueprint(registro)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Laperesayyo1@localhost:3306/check.in"
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    db.create_all()
    app.run()

@app.route('/10', methods=['GET','POST'])
def ten():
    return render_template('10.html')

@app.route('/10pt2', methods=['GET','POST'])
def ten2():
    return render_template('10pt2.html')

