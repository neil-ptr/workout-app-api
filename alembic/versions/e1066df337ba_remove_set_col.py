"""remove 'set' col

Revision ID: e1066df337ba
Revises: ba243dd86293
Create Date: 2021-07-14 00:03:46.794580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1066df337ba'
down_revision = 'ba243dd86293'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('exercise_templates', 'set')


def downgrade():
    pass
