"""Proposal Fields

Revision ID: b57fef00b65d
Revises: 7a3a43f4ffb4
Create Date: 2023-06-21 17:49:43.944677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b57fef00b65d'
down_revision = '7a3a43f4ffb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proposal_field',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('type', sa.Enum('texto', 'número', name='choices'), nullable=False),
    sa.Column('nullable', sa.Boolean(), nullable=False),
    sa.Column('order', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('username', name='user_username_key')
    )
    op.drop_table('proposal_field')
    # ### end Alembic commands ###