import os 
from urllib.request import urlretrieve
import zipfile
from cnnClassifier.config.configuration import DataIngestionConfig 
from cnnClassifier import logging, CustomException

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 
    
    def download_file(self):
        try:
            logging.info(f"Attempting to download file from {self.config.source_url}")
            logging.info(f"Target location: {self.config.local_data_file}")
            os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
            
            if not os.path.exists(self.config.local_data_file):
                file_name, headers = urlretrieve(
                    url= self.config.source_url, 
                    filename=self.config.local_data_file
                )
                logging.info(f"{file_name} downloaded! with the following info: \n{headers}")
            else:
                logging.info(f"File already exists at {self.config.local_data_file}")
        except Exception as e:
            raise CustomException(e)
        
    def extract_zip_file(self):
        logging.info(f"Extracting zip file from: {self.config.local_data_file}")
        logging.info(f"Target extraction directory: {self.config.unzip_dir}")
        try:
            unzip_dir = self.config.unzip_dir 
            os.makedirs(unzip_dir, exist_ok=True)
            if os.path.exists(self.config.local_data_file):
                with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                    zip_ref.extractall(unzip_dir)
            logging.info(f"file extracted to: {unzip_dir}")
        except Exception as e:
            raise CustomException(e)