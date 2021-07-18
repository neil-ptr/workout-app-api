"""add date column

Revision ID: 692e374acca7
Revises: e3a1aafbfaaf
Create Date: 2021-07-16 22:35:49.936388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '692e374acca7'
down_revision = 'e3a1aafbfaaf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('workouts', sa.Column('started', sa.DateTime()))
    op.add_column('workouts', sa.Column('ended', sa.DateTime()))

def downgrade():
    pass
