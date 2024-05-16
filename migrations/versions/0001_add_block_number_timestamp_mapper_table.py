"""add block number <-> timestamp mapper table

Revision ID: e5071ed569e3
Revises: 6a9dce905151
Create Date: 2024-05-15 20:35:21.761611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e5071ed569e3'
down_revision: Union[str, None] = '6a9dce905151'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('block_ts_mapper',
    sa.Column('ts', sa.BIGINT(), nullable=False),
    sa.Column('block_number', sa.BIGINT(), nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('ts')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('block_ts_mapper')
    # ### end Alembic commands ###
