"""Create a baseline migrations

Revision ID: ec2e63d139cf
Revises: 0e1c338eab8e
Create Date: 2024-01-10 12:51:04.252229

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec2e63d139cf'
down_revision: Union[str, None] = '0e1c338eab8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_users', sa.Column('role', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('my_users', 'role')
    # ### end Alembic commands ###