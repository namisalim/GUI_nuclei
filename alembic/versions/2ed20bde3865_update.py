"""update

Revision ID: 2ed20bde3865
Revises: 4dbd79658694
Create Date: 2022-08-23 08:13:00.375087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ed20bde3865'
down_revision = '4dbd79658694'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###
