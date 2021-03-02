"""Initial commit

Revision ID: 8d1063ecfa01
Create Date: 2020-10-26 18:47:04.617473

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "8d1063ecfa01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.VARCHAR(length=6), nullable=False),
        sa.Column("title", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("label", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("text", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="posts_pkey"),
    )


def downgrade():
    op.drop_table("posts")
