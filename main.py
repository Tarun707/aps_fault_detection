from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os

# def test_logger_and_exception():
#      try:
#           logging.info("Starting the test_logger_and_exceptions")
#           result = 3/0
#           print(result)
#           logging.info("Stopping the test_logger_and_exceptions")
#      except Exception as e:
#           logging.debug(str(e))
#           raise SensorException(e, sys)

# if __name__ =="__main__":
#      try:
#           test_logger_and_exception()
#      except Exception as e:
#           print(e)

if __name__=="__main__":
     try:
          get_collection_as_dataframe(database_name="aps", collection_name="sensor")
     except Exception as e:
          print(e)

