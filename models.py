from database import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
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



class Aeroporto(db.Model):
  __tablename__ = 'aeroporto'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  cnpj = db.Column(db.Integer)
  senha = db.Column(db.String(16))
  
  def __init__(self, nome, cnpj, senha):
    self.nome = nome
    self.cnpj = cnpj
    self.senha = senha


class Orientacoes(db.Model):
  __tablename__ = 'orientacoes'
  id = db.Column(db.Integer, primary_key=True)
  descricao = db.Column(db.String(240))
  titulo = db.Column(db.String(100))
  imagem = db.Column(db.String(100))

  def __init__(self, descricao, titulo, imagem):
    self.descricao = descricao
    self.titulo = titulo
    self.imagem = imagem