"""remove foreign key

Revision ID: 714d8b9bf405
Revises: 18d217238852
Create Date: 2021-07-26 22:44:50.660525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '714d8b9bf405'
down_revision = '18d217238852'
branch_labels = None
depends_on = None


def upgrade():
    pass

def downgrade():
    op.drop_constraint('workouts_user_id_fkey', 'workouts', type_='foreignkey')
    op.drop_constraint('workouts_workout_template_id_fkey', 'workouts', type_='foreignkey')


