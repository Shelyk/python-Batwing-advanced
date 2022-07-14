"""001_create_book_table

Revision ID: 001_create_book_table
Revises: 
Create Date: 2022-07-14 11:29:26.394157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_book_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("book")
