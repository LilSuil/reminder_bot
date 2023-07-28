from aiogram.filters import BaseFilter
from aiogram.types import Message
from services import SerializeServices

class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

class CheckDB(BaseFilter):

    def __init__(self, client):
        self.client = client

    async def __call__(self, message: Message) -> bool:
        return bool(await self.client.get(f'USER_DATA-{message.from_user.id}'))

class CheckUserList(BaseFilter):
    def __init__(self, user_id, user_id_list):
        self.user_id = user_id
        self.user_id_list = user_id_list

    async def __call__(self, message: Message) -> bool:
        return self.user_id in self.user_id_list




