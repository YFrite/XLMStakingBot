from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    secret_key: Mapped[Optional[str]] = mapped_column(String(56))

    xlm_in_staking: Mapped[int] = mapped_column(server_default="0")
    xlm_over: Mapped[Optional[int]]

    parent_id: Mapped[Optional[int]]

    def __repr__(self):
        return f"User(id={self.id}, secret_key={self.secret_key}, xlm_in_staking={self.xlm_in_staking}, " \
               f"xlm_over={self.xlm_over}, parent_id={self.parent_id})"
