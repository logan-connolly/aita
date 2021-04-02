"""add timestamp column

Revision ID: 22022a3f6df1
Revises: 8d1063ecfa01
Create Date: 2021-04-01 11:57:16.572356

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "22022a3f6df1"
down_revision = "8d1063ecfa01"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("ts", sa.DateTime))


def downgrade():
    op.drop_column("posts", "ts")
