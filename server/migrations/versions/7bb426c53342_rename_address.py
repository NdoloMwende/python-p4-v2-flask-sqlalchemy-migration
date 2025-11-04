"""rename address

Revision ID: 7bb426c53342
Revises: 3e4fdca51b05
Create Date: 2025-11-04 14:14:01.427043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bb426c53342'
down_revision = '3e4fdca51b05'
branch_labels = None
depends_on = None


def upgrade():
    # SQLite does not support ALTER COLUMN directly, so we recreate the table safely
    with op.batch_alter_table('departments', recreate='always') as batch_op:
        batch_op.alter_column('address', new_column_name='location', existing_type=sa.String(), nullable=False)


def downgrade():
    with op.batch_alter_table('departments', recreate='always') as batch_op:
        batch_op.alter_column('location', new_column_name='address', existing_type=sa.String(), nullable=True)
