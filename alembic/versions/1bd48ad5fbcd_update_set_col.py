"""update set col

Revision ID: 1bd48ad5fbcd
Revises: 40661a31f2da
Create Date: 2021-07-13 23:55:41.022894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bd48ad5fbcd'
down_revision = '40661a31f2da'
branch_labels = None
depends_on = None



def upgrade():
    op.add_column('exercise_templates', sa.Column('sets', sa.Integer()))


def downgrade():    
    op.drop_column('exercise_templates', 'set')
