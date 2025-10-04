import os 
from urllib.request import urlretrieve
import zipfile
from cnnClassifier.config.configuration import DataIngestionConfig 
from cnnClassifier import logging, CustomException

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = urlretrieve(
                url= self.config.source_url, 
                filename=self.config.local_data_file
            )
            logging.info(f"{file_name} download! with the following info: \n{headers}")
        else:
            logging.info(f"already exist.")

        
    def extract_zip_file(self):
        logging.info(f"extracting zip file: {self.config.local_data_file}....")

        unzip_dir = self.config.unzip_dir 
        os.makedirs(unzip_dir, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_dir)
        logging.info(f"file extracted to: {unzip_dir}")
