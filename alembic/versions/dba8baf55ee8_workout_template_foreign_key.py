"""workout template foreign key

Revision ID: dba8baf55ee8
Revises: f3c4ed928dbd
Create Date: 2021-07-26 22:05:05.062043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dba8baf55ee8'
down_revision = 'f3c4ed928dbd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('workouts',
        sa.Column('workout_template_id', sa.Integer, sa.ForeignKey('users.id'))
    )


def downgrade():
    pass
