"""User passwrod length increase

Revision ID: 18b142e0011b
Revises: c5684b187e2f
Create Date: 2024-01-15 14:06:39.656567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18b142e0011b'
down_revision: Union[str, None] = 'c5684b187e2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('my_users', 'password',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=526),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('my_users', 'password',
               existing_type=sa.String(length=526),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###