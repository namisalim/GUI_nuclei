"""update

Revision ID: 95222051d9cb
Revises: bac52b76c543
Create Date: 2022-08-22 09:41:27.055642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95222051d9cb'
down_revision = 'bac52b76c543'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('usertype', sa.String(), nullable=True))
    op.drop_column('users', 'ver_code')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('ver_code', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'usertype')
    # ### end Alembic commands ###
