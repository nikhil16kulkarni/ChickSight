from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.components.evaluation import Evaluation
from ChickenDiseaseClassification.components.prepare_callbacks import PrepareCallback
from ChickenDiseaseClassification.components.training import Training
from ChickenDiseaseClassification.entity.config_entity import *
from ChickenDiseaseClassification.config.configuration import *
from ChickenDiseaseClassification.components.prepare_base_model import *


STAGE_NAME = "EVALUATION"

class EvaluationPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")

        obj = EvaluationPipeline()

        obj.main()

        logger.info(f"Completed {STAGE_NAME} pipeline...")

    except Exception as e:
        logger.exception(e)
        raise e
