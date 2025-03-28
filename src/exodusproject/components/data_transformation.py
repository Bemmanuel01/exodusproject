import os
from src.exodusproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.exodusproject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        
    ## Add every data transformation technique here e.g scaler, PCA, train_test split
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        
        ## Split data into training and testing sets (0.75, 0.25) respectively
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        logger.info("Split data into training & testing sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)