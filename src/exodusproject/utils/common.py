import os
import yaml
from src.exodusproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

## Reading the yaml path
@ensure_annotations
def read_yaml(path_to_yaml: Path):
    """ Reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox:ConfigBox type
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
    
# Creating directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool =True):
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log(bool, optional) ignore if multiple dirs is to be created. Default to
        
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        
        if verbose:
            logger.info(f"Created directory at: {path}")
            
## Saving file to json
@ensure_annotations
def save_json(path: Path, data: dict):
    """Save Json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"Json file saved at: {path}")
    
## Load the json file data
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load Json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attribute instead of dict
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

## Saving the model
@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save the binary file containing the model

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved successfully at: {path}")
    
## Loading the model form the binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary data

    Args:
        path (Path): path to binary file 

    Returns:
        Any: Object stored in the file
    """
    
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully at: {path}")
    return data

