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
