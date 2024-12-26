import os
from dataclasses import dataclass
from datetime import datetime
from ewasteDetection.constant.training_pipeline import *


@dataclass
class TrainingPipelineConfig:
    """
    Configuration for the training pipeline.
    
    Attributes:
    - artifacts_dir: Directory to store all artifacts generated during the pipeline.
    """
    artifacts_dir: str = ARTIFACTS_DIR
    
    
# Initialize the main training pipeline configuration    
training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    """
    Configuration for the data ingestion process.

    Attributes:
    - data_ingestion_dir: Directory to store data ingestion artifacts.
    - feature_store_file_path: Path to the feature store where processed data is stored.
    - data_download_url: URL to download the dataset.
    """
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        DATA_INGESTION_DIR_NAME
    )
    
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, 
        DATA_INGESTION_FEATURE_STORE_DIR
    )
    
    data_download_url: str = DATA_DOWNLOAD_DIR
    
    
@dataclass
class DataValidationConfig:
    """
    Configuration for the data validation process.

    Attributes:
    - data_validation_dir: Directory to store data validation artifacts.
    - valid_status_file_dir: Path to the file containing validation status.
    - required_file_list: List of files required for data validation.
    """
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        DATA_VALIDATION_DIR_NAME
    )
    
    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
    
    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES
    
    
@dataclass
class ModelTrainerConfig:
    """
    Configuration for the model training process.

    Attributes:
    - model_trainer_dir: Directory to store model training artifacts.
    - weight_name: Name of the pre-trained weights to be used for training.
    - no_epochs: Number of epochs for model training.
    - batch_size: Batch size for model training.
    """
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        MODEL_TRAINER_DIR_NAME
    )
    
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    
    no_epochs = MODEL_TRAINER_NO_EPOCHS
    
    batch_size = MODEL_TRAINER_BATCH_SIZE