"""convert int to float

Revision ID: 69d55edde990
Revises: 03c7730fd697
Create Date: 2026-04-28 12:05:55.105845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69d55edde990'
down_revision: Union[str, Sequence[str], None] = '03c7730fd697'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
