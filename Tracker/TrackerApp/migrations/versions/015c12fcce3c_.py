"""empty message

Revision ID: 015c12fcce3c
Revises: 95d2a86ef612
Create Date: 2024-01-07 15:35:50.711729

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '015c12fcce3c'
down_revision = '95d2a86ef612'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.String(length=128),
               existing_nullable=True)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.String(length=128),
               existing_nullable=True)
        batch_op.alter_column('first_name',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.String(length=128),
               existing_nullable=True)
        batch_op.alter_column('last_name',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.String(length=128),
               existing_nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=True)
        batch_op.alter_column('first_name',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=True)

    # ### end Alembic commands ###
