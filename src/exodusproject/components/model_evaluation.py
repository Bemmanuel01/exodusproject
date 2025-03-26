import os
import pandas as pd
import numpy as np
import mlflow
import joblib
import mlflow.sklearn
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse

from src.exodusproject.entity.config_entity import ModelEvaluationConfig
from src.exodusproject.constants import *
from src.exodusproject.utils.common import read_yaml, create_directories, save_json

# os.environ["MLFLOW_TRACKING_URL"] = "https://dagshub.com/Bemmanuel01/exodusproject.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"] = "Bemmanuel01"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "e353837df0e25a5c9bcc2f189b45f8d00c437685"

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_squared_error(actual, pred)
        r2 = r2_score(actual, pred)
        
        return rmse, mae, r2
    
    ## Log into mlflow
    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            ## Saving the metrics as local
            
            scores = {"rmse":rmse, "mae":mae, "r2":r2}
            save_json(path=Path(self.config.metric_file_name), data = scores)
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            
            
            ## Model registry does not work with file store
            if tracking_uri_type_store != "file":
                ## Register the model
                
                mlflow.sklearn.log_model(model, "model", registered_model_name="Elasticnetmodel")
                
            else:
                mlflow.sklearn.log_model(model,"model")