"""template foreign key

Revision ID: 18d217238852
Revises: dba8baf55ee8
Create Date: 2021-07-26 22:36:24.362479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18d217238852'
down_revision = 'dba8baf55ee8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('workouts',
        sa.Column('workout_template_id', sa.Integer, sa.ForeignKey('workout_templates.id'))
    )


def downgrade():
    pass
