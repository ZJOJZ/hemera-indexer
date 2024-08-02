"""add user ops table

Revision ID: 9a1e927f02bb
Revises: 3d5ce8939570
Create Date: 2024-07-31 13:11:10.244802

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "9a1e927f02bb"
down_revision: Union[str, None] = "3d5ce8939570"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_operations_results",
        sa.Column("user_op_hash", postgresql.BYTEA(), nullable=False),
        sa.Column("sender", sa.VARCHAR(length=42), nullable=True),
        sa.Column("paymaster", sa.VARCHAR(length=42), nullable=True),
        sa.Column("nonce", sa.NUMERIC(), nullable=True),
        sa.Column("status", sa.BOOLEAN(), nullable=True),
        sa.Column("actual_gas_cost", sa.NUMERIC(), nullable=True),
        sa.Column("actual_gas_used", sa.INTEGER(), nullable=True),
        sa.Column("init_code", postgresql.BYTEA(), nullable=True),
        sa.Column("call_data", postgresql.BYTEA(), nullable=True),
        sa.Column("call_gas_limit", sa.INTEGER(), nullable=True),
        sa.Column("verification_gas_limit", sa.INTEGER(), nullable=True),
        sa.Column("pre_verification_gas", sa.INTEGER(), nullable=True),
        sa.Column("max_fee_per_gas", sa.INTEGER(), nullable=True),
        sa.Column("max_priority_fee_per_gas", sa.INTEGER(), nullable=True),
        sa.Column("paymaster_and_data", postgresql.BYTEA(), nullable=True),
        sa.Column("signature", postgresql.BYTEA(), nullable=True),
        sa.Column("transactions_hash", postgresql.BYTEA(), nullable=True),
        sa.Column("transactions_index", sa.INTEGER(), nullable=True),
        sa.Column("block_number", sa.INTEGER(), nullable=True),
        sa.Column("block_timestamp", postgresql.TIMESTAMP(), nullable=True),
        sa.Column("bundler", sa.VARCHAR(length=42), nullable=True),
        sa.Column("start_log_index", sa.INTEGER(), nullable=True),
        sa.Column("end_log_index", sa.INTEGER(), nullable=True),
        sa.PrimaryKeyConstraint("user_op_hash"),
    )
    op.create_index(
        "transactions_hash_index",
        "user_operations_results",
        ["transactions_hash"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("transactions_hash_index", table_name="user_operations_results")
    op.drop_table("user_operations_results")
    # ### end Alembic commands ###
