import pickle

class SerializeServices:

    @staticmethod
    async def serialize(obj: any) -> bytes:
        return pickle.dumps(obj)

    @staticmethod
    async def deserialize(obj: bytes) -> any:
        return pickle.loads(obj)

