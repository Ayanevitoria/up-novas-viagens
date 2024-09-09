from flask import Flask, render_template, request, redirect, url_for, flash
from database import db,lm
from flask_migrate import Migrate
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from models import Usuario
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'up123viagens'


conexao = 'mysql+pymysql://anakezia:Ann%401500@db4free.net/bancoddedadoskez'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
lm.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@lm.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and senha == usuario.senha:
            login_user(usuario)
            return redirect(url_for('index'))
        else:
            flash('Email ou senha inválidos', 'error')
            return redirect(url_for('login'))


@app.route('/usuariorecovery')
@login_required
def usuariorecovery():
    if current_user.admin == 0:
        return redirect('/login')

    user=Usuario.query.all()
    return render_template('usuario_recovery.html', user=user)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'GET':
    return render_template('cadastro.html')
  if request.method == 'POST':
    primeironome = request.form.get('primeironome')
    sobrenome = request.form.get('sobrenome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    user = Usuario(primeironome,sobrenome,email,senha,0)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
