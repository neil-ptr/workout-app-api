"""create set col

Revision ID: 40661a31f2da
Revises: 
Create Date: 2021-07-13 23:39:18.689710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40661a31f2da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('exercise_templates', sa.Column('set', sa.Integer()))


def downgrade():
    pass
