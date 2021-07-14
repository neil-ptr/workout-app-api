"""remove 'set' col

Revision ID: ba243dd86293
Revises: 1bd48ad5fbcd
Create Date: 2021-07-13 23:58:22.907848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba243dd86293'
down_revision = '1bd48ad5fbcd'
branch_labels = None
depends_on = None


def upgrade(): 
    op.drop_column('exercise_templates', 'set')


def downgrade():
    pass
