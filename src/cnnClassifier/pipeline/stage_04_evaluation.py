from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation

class EvaluationPipeline:
    def main(self):
        config = ConfigurationManager() 
        eval_config = config.get_evaluation_config() 
        evalutaion = Evaluation(config = eval_config)
        evalutaion.evaluation()
        evalutaion.save_scores()