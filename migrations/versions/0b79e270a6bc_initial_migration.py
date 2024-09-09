"""Initial migration

Revision ID: 0b79e270a6bc
Revises: 
Create Date: 2024-09-09 12:25:00.130763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b79e270a6bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aeroporto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('cnpj', sa.Integer(), nullable=True),
    sa.Column('senha', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orientacoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=240), nullable=True),
    sa.Column('titulo', sa.String(length=100), nullable=True),
    sa.Column('imagem', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('primeironome', sa.String(length=100), nullable=True),
    sa.Column('sobrenome', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('senha', sa.String(length=16), nullable=True),
    sa.Column('admin', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('orientacoes')
    op.drop_table('aeroporto')
    # ### end Alembic commands ###
