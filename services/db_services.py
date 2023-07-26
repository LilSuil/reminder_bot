from database import redisClient
from services.serialize_services import SerializeServices


class FastDbServices:

    def __init__(self):
        self.serializeServices = SerializeServices()

    async def collectUser_in_RedisUsersDict(self, user_id=None) -> None:
        if await redisClient.get('ALL_USERS') is None:
            await redisClient.set(name='ALL_USERS', value=await self.serializeServices.serialize({'all_users': []}))
            print('good')

        base = await self.serializeServices.deserialize(await redisClient.get('ALL_USERS'))
        if user_id not in base['all_users'] and user_id != None:
            base['all_users'].append(user_id)
            await redisClient.set(name='ALL_USERS', value=await self.serializeServices.serialize(base))


