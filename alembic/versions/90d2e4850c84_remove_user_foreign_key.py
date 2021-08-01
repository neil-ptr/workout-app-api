"""remove user foreign key

Revision ID: 90d2e4850c84
Revises: bd04e8a73cd1
Create Date: 2021-07-26 23:01:55.002917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d2e4850c84'
down_revision = 'bd04e8a73cd1'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('workouts_user_id_fkey', 'workouts', type_='foreignkey')
    op.drop_constraint('workouts_workout_template_id_fkey', 'workouts', type_='foreignkey')
    op.drop_column('workouts', 'workout_template_id')


def downgrade():
    pass
