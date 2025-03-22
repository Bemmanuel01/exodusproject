from src.exodusproject.config.configuration import ConfigurationManager
from src.exodusproject.components.data_ingestion import DataIngestion
from src.exodusproject import logger

## Defining the pipeline stage
STAGE_NAME = "Data Ingestion Stage"

## Data ingestion pipeline class
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiated_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiated_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n x==========x")
        
    except Exception as e:
        logger.execution(e)
        raise e