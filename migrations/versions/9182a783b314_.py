"""empty message

Revision ID: 9182a783b314
Revises: 50cc8c5368f1
Create Date: 2021-09-19 01:14:02.321846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9182a783b314'
down_revision = '50cc8c5368f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('protector',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mode_value', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('protector_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['protector_id'], ['protector.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permission')
    op.drop_table('protector')
    # ### end Alembic commands ###
