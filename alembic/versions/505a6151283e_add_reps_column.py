"""add reps column

Revision ID: 505a6151283e
Revises: 
Create Date: 2021-12-25 23:30:02.452942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505a6151283e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('exercise_templates', sa.Column('reps', sa.Integer()))


def downgrade():
    pass
