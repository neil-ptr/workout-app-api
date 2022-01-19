"""remove active duration from exercises

Revision ID: 1937eeb159be
Revises: cd359a797a75
Create Date: 2022-01-01 00:36:20.213379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1937eeb159be'
down_revision = 'cd359a797a75'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('exercises', 'duration')


def downgrade():
    pass
