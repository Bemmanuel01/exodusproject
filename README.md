# End to End DataScience Project Structure and Workflow

### Workflows -- ML Pipeline
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation


## Workflow - Data Ingestion
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py

## Summary of the configuration manager
Reads configuration files (config.yaml, params.yaml, schema.yaml).
Creates required directories (like artifacts_root and data_ingestion.root_dir).
Returns a structured DataIngestionConfig object to be used in the ingestion pipeline.

## Summary of the components
Checks if the dataset is already downloaded; if not, it downloads it.
Extracts the downloaded ZIP file to a specified folder.
Uses logging to track progress.
Creates necessary directories if they don’t exist.

## Summary of the Pipeline:
Imports necessary modules (ConfigurationManager, DataIngestion, logger).
Defines a pipeline class (DataIngestionTrainingPipeline) for managing data ingestion.
Creates directories, downloads the dataset, and extracts it.
Implements error handling to log any issues.
Ensures proper execution flow with if __name__ == "__main__".