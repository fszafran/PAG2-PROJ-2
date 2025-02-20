import pymongo
import redis
import os
from dotenv import load_dotenv
load_dotenv()

#mongo setup
url = "mongodb://localhost:27017"
mongo_client = pymongo.MongoClient(url)
mongo_db = mongo_client['pag2']

#redis setup
redis_db = redis.Redis(
    host= str(os.getenv("REDIS_HOST")),
    port=18568,
    decode_responses=True,
    username="default",
    password=str(os.getenv("REDIS_PASSWORD")),
)