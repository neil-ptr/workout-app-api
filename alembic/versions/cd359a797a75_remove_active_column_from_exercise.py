"""remove active column from exercise

Revision ID: cd359a797a75
Revises: 505a6151283e
Create Date: 2022-01-01 00:32:38.691636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd359a797a75'
down_revision = '505a6151283e'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('exercises', 'active')


def downgrade():
    pass
