"""update proposal

Revision ID: 9f019226fcb9
Revises: b72e3e2dc96c
Create Date: 2023-06-22 16:19:38.347279

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "9f019226fcb9"
down_revision = "b72e3e2dc96c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("proposal", schema=None) as batch_op:
        batch_op.alter_column(
            "status",
            existing_type=postgresql.ENUM(
                "aprovado", "negado", "pendente", name="status"
            ),
            type_=sa.String(length=10),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("proposal", schema=None) as batch_op:
        batch_op.alter_column(
            "status",
            existing_type=sa.String(length=10),
            type_=postgresql.ENUM("aprovado", "negado", "pendente", name="status"),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
