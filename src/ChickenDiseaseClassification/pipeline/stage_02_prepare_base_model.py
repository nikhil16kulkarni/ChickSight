from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.entity.config_entity import *
from ChickenDiseaseClassification.config.configuration import *
from ChickenDiseaseClassification.components.prepare_base_model import *

STAGE_NAME = "PREPARE BASE MODEL"

class PrepareBaseModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        obj = PrepareBaseModelTrainingPipeline()

        obj.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

    except Exception as e:
        logger.exception(e)
        raise e
