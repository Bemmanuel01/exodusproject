from src.exodusproject import logger
from src.exodusproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.exodusproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.exodusproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiated_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n x==========x")
        
except Exception as e:
    logger.execution(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} complete <<<<<<\n\n x==========x")
    
except Exception as e:
    logger.exception(e)
    raise e
    
    
STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} complete <<<<<<\n\n x==========x")
    
except Exception as e:
    logger.exception(e)
    raise e
