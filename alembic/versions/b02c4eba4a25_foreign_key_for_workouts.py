"""foreign key for workouts

Revision ID: b02c4eba4a25
Revises: ac7ced14e3ae
Create Date: 2021-07-27 21:16:43.818867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b02c4eba4a25'
down_revision = 'ac7ced14e3ae'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('workouts', sa.Column('workout_template_id', sa.Integer, sa.ForeignKey('workout_templates.id'), nullable=False))
    # op.create_foreign_key('workouts_workout_templates_fk','workouts', 'workout_templates',['workout_template_id'], ['id'])


def downgrade():
    pass
