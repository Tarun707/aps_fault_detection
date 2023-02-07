import pymongo
import pandas as pd
import json
import os
from dataclasses import dataclass

@dataclass
class EnvironmentVariable:
    mongo_db_url = os.getenv("MONGO_DB_URL")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_id = os.getenv("AWS_ACCESS_SECRET_ID")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"