from cnnClassifier import CustomException, logging
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel


class PrepareBaseModelPipeline:
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model() 
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    STAGE_NAME = "prepare base model"
    try:
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
        prepare_base_model = PrepareBaseModelPipeline() 
        prepare_base_model.main()
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

    except Exception as e:
        raise CustomException(e)