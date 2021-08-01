"""remove foreign key

Revision ID: ac7ced14e3ae
Revises: f300b6047c01
Create Date: 2021-07-26 23:14:05.038641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac7ced14e3ae'
down_revision = 'f300b6047c01'
branch_labels = None
depends_on = None


def upgrade():
    # op.drop_constraint(constraint_name="workouts_workout_template_id_fkey", table_name="workouts", type_="foreignkey")
    pass


def downgrade():
    pass
