import pandas as pandas
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os, sys

def get_collection_as_dataframe(database_name, collection_name)->pd.DataFrame:
    try:
        logging.info(f"Reading data from database: {database_name} and collection {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns: {df.columns}")
        if "_id" in df.columns:
            logging.info("Dropping columns: _id")
            df = df.drop("_id", axis=1)
        logging.info(f"Rows and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)
