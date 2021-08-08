"""workout id column

Revision ID: 99b62bf8111b
Revises: 73c6fe65bf62
Create Date: 2021-08-04 22:00:51.404153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99b62bf8111b'
down_revision = '73c6fe65bf62'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('exercises',
                  sa.Column('workout_id', sa.Integer,
                            sa.ForeignKey('workouts.id'))
                  )


def downgrade():
    pass
