import sys, os
from ewasteDetection.logger import logging
from ewasteDetection.exception import AppException
from ewasteDetection.components.data_ingestion import DataIngestion
from ewasteDetection.components.data_validation import DataValidation
from ewasteDetection.components.model_trainer import ModelTrainer

from ewasteDetection.entity.config_entity import (DataIngestionConfig,
                                               DataValidationConfig,
                                               ModelTrainerConfig)

from ewasteDetection.entity.artifacts_entity import (DataIngestionArtifact,
                                                  DataValidationArtifact,
                                                  ModelTrainerArtifact)

class TrainPipeline:
    """
    This class orchestrates the entire training pipeline, including data ingestion, 
    data validation, and model training.
    """
    
    def __init__(self):
        """
        Constructor to initialize configuration objects for each pipeline stage.
        """
        self.data_ingestion_config = DataIngestionConfig() #  Configuration for data ingestion
        self.data_validation_config = DataValidationConfig() # Configuration for data validation
        self.model_trainer_config = ModelTrainerConfig() # Configuration for model training
        
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiates the data ingestion process.

        :return: DataIngestionArtifact containing paths to the downloaded and processed data.
        :raises AppException: If data ingestion fails.
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from URL")
            
            # Create an instance of the DataIngestion class
            data_ingestion = DataIngestion(
                data_ingestion_config= self.data_ingestion_config
            )
            
            # Execute data ingestion and retrieve artifacts
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info("Exit the start_data_ingestion of TrainPipeline class")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e, sys)
        

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        Initiates the data validation process.

        :param data_ingestion_artifact: Artifact containing paths to ingested data.
        :return: DataValidationArtifact containing validation status.
        :raises AppException: If data validation fails.
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")
        
        try:
            # Create an instance of the DataValidation class
            data_validation = DataValidation(
                data_ingestion_artifact = data_ingestion_artifact,
                data_validation_config = self.data_validation_config
            )
        
            # Execute data validation and retrieve artifacts
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Performed the data validation operation")
            logging.info("Exit the start_data_validation of TrainPipeline class")
            
            return data_validation_artifact
        
        except Exception as e:
            raise AppException(e, sys)
            
    
    def start_model_trainer(self) -> ModelTrainerArtifact:
        """
        Initiates the model training process.

        :return: ModelTrainerArtifact containing the path to the trained model.
        :raises AppException: If model training fails.
        """
        try:
            # Create an instance of the ModelTrainer class
            model_trainer = ModelTrainer(
                model_trainer_config = self.model_trainer_config
            )
            
            # Execute model training and retrieve artifacts
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            
            return model_trainer_artifact
        
        except Exception as e:
            raise AppException(e, sys)
       
     
    def run_pipeline(self) -> None:
        """
        Runs the entire training pipeline, including:
        - Data ingestion
        - Data validation
        - Model training (if validation is successful)

        :raises AppException: If any stage of the pipeline fails.
        """
        try:
            # Step 1: Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()
            
            # Step 2: Data Validation
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact = data_ingestion_artifact
            )
            
            # Step 3: Model Training (if validation is successful)
            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception("Your data is not in correct format")
        
        except Exception as e:
            raise AppException(e, sys)
