from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallbacks
from cnnClassifier.components.training import Training
from cnnClassifier import logging, CustomException

class TrainingPipeline:
    def main(self):
        config = ConfigurationManager() 
        # prepare callbacks 
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        # training 
        training_config = config.get_training_config() 
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list = callback_list)

if __name__ == "__main__":
    STAGE_NAME = "train the model"
    try:
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
        training = TrainingPipeline() 
        training.main()
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

    except Exception as e:
        raise CustomException(e)