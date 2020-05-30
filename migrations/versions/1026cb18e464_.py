"""empty message

Revision ID: 1026cb18e464
Revises: 
Create Date: 2020-05-30 06:43:02.860299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1026cb18e464'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registration')
    op.drop_table('login')
    # ### end Alembic commands ###