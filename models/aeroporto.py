from database import db

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
