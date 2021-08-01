"""default 'ended' value

Revision ID: f3c4ed928dbd
Revises: 692e374acca7
Create Date: 2021-07-26 20:09:25.045039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3c4ed928dbd'
down_revision = '692e374acca7'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('workouts', 'ended', nullable=True)


def downgrade():
    pass
