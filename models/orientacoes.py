from database import db

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