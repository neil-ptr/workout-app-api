"""remove workout_template_d col

Revision ID: f300b6047c01
Revises: 90d2e4850c84
Create Date: 2021-07-26 23:11:01.490018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f300b6047c01'
down_revision = '90d2e4850c84'
branch_labels = None
depends_on = None


def upgrade():
    # op.drop_column('workouts', 'workout_template_id')
    # op.drop_constraint(constraint_name="workouts_workout_template_id_fkey", table_name="workouts", type_="foreignkey")
    pass



def downgrade():
    pass
