from sqlalchemy.ext.asyncio import AsyncSession

from core.base.repository import BaseRepository
from domains.users import User
from utils.condition_builder import ConditionBuilder


class UserRepository(BaseRepository[User]):

    def __init__(self, session: AsyncSession, condition_builder: ConditionBuilder):
        super().__init__(User, session, condition_builder)
