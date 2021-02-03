import redis
import os

class Storage:

    def __init__(self):
        self.r = redis.Redis(
            host=os.environ.get('REDIS_HOST'),
            port=os.environ.get('REDIS_PORT'),
            db=0
        )

    def set(self, key, value): return self.r.set(key, value)
    def get(self, key): return self.r.get(key)
    def count(self): return len(list(self.r.scan_iter("*")))
