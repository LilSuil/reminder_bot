import redis.asyncio as redis

redisClient = redis.StrictRedis(host='localhost', db=1, port=6379)

