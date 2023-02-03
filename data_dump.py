import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert DataFrame to JSON so that we can dump these records in mongoDB
    df.reset_index(drop=True, inplace=True) # Dropping the index
    # .to_json converts df to json object and json_loads convert json object into python dictionary
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # insert converted json records to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

