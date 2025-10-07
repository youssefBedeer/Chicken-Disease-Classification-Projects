import yaml
from box import ConfigBox 
from ensure import ensure_annotations 
from cnnClassifier import CustomException, logging
import os
from pathlib import Path
import json
import base64

@ensure_annotations
def read_yaml(yaml_file_path:Path)-> ConfigBox:
    """
    reads yaml file 

    Args:
        path to yaml file (Path)

    Returns: 
        ConfigBox type
    """
    with open(yaml_file_path, "r") as f:
        content = ConfigBox(yaml.safe_load(f))
        logging.info(f"reading yaml file -> {yaml_file_path} successed.")
    return content




@ensure_annotations
def create_directories(list_of_directories:list):
    """
    make directories 
    
    Args:
        list of directories wants to create
    
    """
    for path in list_of_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            logging.info(f"folder created at '{path}'")
        else:
            logging.info(f"folder '{path}' already exist.")


@ensure_annotations 
def save_json(path:Path, data:dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


@ensure_annotations 
def load_json(path:Path) ->ConfigBox:
    with open(path) as f:
        content = json.laod(f)

    logging.info(f"json file loaded succesfully from : {path}")
    return ConfigBox(content)


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())