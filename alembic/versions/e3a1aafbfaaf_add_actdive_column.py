"""add actdive column

Revision ID: e3a1aafbfaaf
Revises: e1066df337ba
Create Date: 2021-07-16 22:33:04.953093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3a1aafbfaaf'
down_revision = 'e1066df337ba'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('workouts', sa.Column('active', sa.Boolean()))


def downgrade():
    pass
