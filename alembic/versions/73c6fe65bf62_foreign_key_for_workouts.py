"""foreign key for workouts

Revision ID: 73c6fe65bf62
Revises: b02c4eba4a25
Create Date: 2021-07-27 21:44:32.580054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73c6fe65bf62'
down_revision = 'b02c4eba4a25'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('workouts', 'name')


def downgrade():
    pass
