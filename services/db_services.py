from database import redisClient
from services.serialize_services import SerializeServices
from loader import admin_list
import time


class DbServices:

    def __init__(self):
        self.serializeServices = SerializeServices()

    async def collectUser_in_DB(self, user_id) -> None:


        if await redisClient.get(f'USER_DATA-{user_id}') is None:
            await redisClient.set(name=f'USER_DATA-{user_id}',
                                  value=await self.serializeServices.serialize({f'USER_DATA-{user_id}':
                                      {

                                          'user-id': '',
                                          'register-date': '',
                                          'isAdmin': '',

                                      }}))

        base = await self.serializeServices.deserialize(await redisClient.get(f'USER_DATA-{user_id}'))
        if base[f'USER_DATA-{user_id}']['user-id'] == '' and user_id != None:

            base[f'USER_DATA-{user_id}']['user-id'] = user_id
            base[f'USER_DATA-{user_id}']['register-date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())

            if user_id in admin_list:
                base[f'USER_DATA-{user_id}']['isAdmin'] = 'true'
            else:
                base[f'USER_DATA-{user_id}']['isAdmin'] = 'false'

            s = await self.serializeServices.serialize(base)
            await redisClient.set(name=f'USER_DATA-{user_id}', value=s)

            await redisClient.sadd('USERS', user_id)

    async def get_users_list(self) -> list:

        susers = list(await redisClient.smembers('USERS'))
        users = [user.decode('utf-8') for user in susers]

        return users







