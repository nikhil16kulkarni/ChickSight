from ChickenDiseaseClassification import logger

# logger.info("Welcome to my custom log");

from ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import *

STAGE_NAME = "DATA INGESTION"

try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        data_ingestion = DataIngestionTrainingPipeline()

        data_ingestion.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

except Exception as e:
    logger.exception(e)
    raise e
