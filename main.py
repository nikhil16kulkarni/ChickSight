from ChickenDiseaseClassification import logger

# logger.info("Welcome to my custom log");

from ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import *
from ChickenDiseaseClassification.pipeline.stage_02_prepare_base_model import *
from ChickenDiseaseClassification.pipeline.stage_03_training import *
from ChickenDiseaseClassification.pipeline.stage_04_evaluation import *


STAGE_NAME = "DATA INGESTION"

try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        data_ingestion = DataIngestionTrainingPipeline()

        data_ingestion.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "PREPARE BASE MODEL"

try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        data_ingestion = PrepareBaseModelTrainingPipeline()

        data_ingestion.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "TRAINING"

try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        data_ingestion = ModelTrainingPipeline()

        data_ingestion.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "EVALUATION"

try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        data_ingestion = EvaluationPipeline()

        data_ingestion.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

except Exception as e:
    logger.exception(e)
    raise e
