"""remove user foreign key

Revision ID: bd04e8a73cd1
Revises: 714d8b9bf405
Create Date: 2021-07-26 22:52:14.342831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd04e8a73cd1'
down_revision = '714d8b9bf405'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_constraint('workouts_user_id_fkey', 'workouts', type_='foreignkey')
    op.drop_constraint('workouts_workout_template_id_fkey', 'workouts', type_='foreignkey')
