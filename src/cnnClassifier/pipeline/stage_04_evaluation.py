from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logging, CustomException
class EvaluationPipeline:
    def main(self):
        config = ConfigurationManager() 
        eval_config = config.get_evaluation_config() 
        evalutaion = Evaluation(config = eval_config)
        evalutaion.evaluation()
        evalutaion.save_scores()



if __name__ == "__main__":
    STAGE_NAME = "evaluate the model"
    try:
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
        evaluation = EvaluationPipeline() 
        evaluation.main()
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

    except Exception as e:
        raise CustomException(e)