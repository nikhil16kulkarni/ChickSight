from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.entity.config_entity import *
from ChickenDiseaseClassification.config.configuration import *
from ChickenDiseaseClassification.components.data_ingestion import *

STAGE_NAME = "DATA INGESTION"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        obj = DataIngestionTrainingPipeline()

        obj.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

    except Exception as e:
        logger.exception(e)
        raise e


