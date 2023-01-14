from typing import Optional

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.user import User


class UserRepository:

    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, user_id: int, parent_id: Optional[int]):
        user = User(id=user_id, parent_id=parent_id)
        self._session.add(user)
        await self._session.commit()
        return user.id

    async def get(self, user_id: Optional[int] = None, parent_id: Optional[int] = None) -> User:
        if not (user_id or parent_id):
            raise ValueError("user_id or parent_id must be provided")

        return (await self._session.execute(select(User)
                                            .where(
                                                   User.id == user_id))).scalar_one()

    async def is_exists(self, user_id: int):
        return (await self._session.execute(select(User)
                                            .where(User.id == user_id))).scalar_one_or_none() is not None
