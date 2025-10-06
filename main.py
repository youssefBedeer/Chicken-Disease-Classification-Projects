from cnnClassifier import logging, CustomException 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "data ingestion stage"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    data_ingestion = DataIngestionTrainingPipeline() 
    data_ingestion.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)



STAGE_NAME = "prepare base model"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    prepare_base_model = PrepareBaseModelPipeline() 
    prepare_base_model.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)


STAGE_NAME = "train the model"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    training = TrainingPipeline() 
    training.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)


STAGE_NAME = "evaluate the model"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    evaluation = EvaluationPipeline() 
    evaluation.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)