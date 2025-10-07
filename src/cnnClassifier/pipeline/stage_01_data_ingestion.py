from cnnClassifier.config.configuration import ConfigurationManager 
from cnnClassifier.components.data_ingestion import DataIngestion 
from cnnClassifier import logging, CustomException



class DataIngestionTrainingPipeline:
    def main(self):
        config = ConfigurationManager() 
        data_ingestion_config = config.get_data_ingestion_config() 
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    STAGE_NAME = "data ingestion stage"
    try:
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
        data_ingestion = DataIngestionTrainingPipeline() 
        data_ingestion.main()
        logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

    except Exception as e:
        raise CustomException(e)
