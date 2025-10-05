from cnnClassifier import logging, CustomException 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline() 
    data_ingestion.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    raise CustomException(e)



STAGE_NAME = "prepare base model"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelPipeline() 
    prepare_base_model.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    raise CustomException(e)


STAGE_NAME = "train the model"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    training = TrainingPipeline() 
    training.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    raise CustomException(e)