from database import db

class Usuario(db.Model):
  __tablename__ = 'usuario'
  id = db.Column(db.Integer, primary_key=True)
  primeironome = db.Column(db.String(100))
  sobrenome = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)
  senha = db.Column(db.String(16))
  admin = db.Column(db.Integer)

  def __init__(self, primeironome, sobrenome, email, senha, admin):
    self.primeironome = primeironome
    self.sobrenome = sobrenome
    self.email = email
    self.senha = senha
    self.admin = admin