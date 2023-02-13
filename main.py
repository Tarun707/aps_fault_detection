from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity import config_entity
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer

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

# if __name__=="__main__":
#      try:
#           df = get_collection_as_dataframe(database_name="aps", collection_name="sensor")
#           print(df)
#      except Exception as e:
#           print(e)

if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
          print(data_ingestion_artifact)
          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
          data_validation_artifact = data_validation.initiate_data_validation()
          print(data_validation_artifact)
          data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
          data_transformation = DataTransformation(data_transformation_config, data_ingestion_artifact)
          data_transformation_artifact = data_transformation.initiate_data_transformation()
          print(data_transformation_artifact)
          model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
          model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact = model_trainer.initiate_model_trainer()
     except Exception as e:
          print(e)