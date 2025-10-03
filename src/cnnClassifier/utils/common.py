import yaml
from box import ConfigBox 
from ensure import ensure_annotations 
from cnnClassifier import CustomException, logging
import os
from pathlib import Path


@ensure_annotations
def read_yaml(yaml_file_path:Path)-> ConfigBox:
    """
    reads yaml file 

    Args:
        path to yaml file (Path)

    Returns: 
        ConfigBox type
    """
    try:
        with open(yaml_file_path, "r") as f:
            content = ConfigBox(yaml.safe_load(f))
            logging.info(f"reading yaml file -> {yaml_file_path} successed.")
        return content
    except Exception as e:
        raise CustomException(e)



@ensure_annotations
def create_directories(list_of_directories:list):
    """
    make directories 
    
    Args:
        list of directories wants to create
    
    """
    try:
        for path in list_of_directories:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
                logging.info(f"folder created at '{path}'")
            else:
                logging.info(f"folder '{path}' already exist.")
    except Exception as e:
        raise CustomException(e)