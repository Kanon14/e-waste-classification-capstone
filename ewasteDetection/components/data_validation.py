import os, sys
import shutil
from ewasteDetection.logger import logging
from ewasteDetection.exception import AppException
from ewasteDetection.entity.config_entity import DataValidationConfig
from ewasteDetection.entity.artifacts_entity import (DataIngestionArtifact,
                                                    DataValidationArtifact)


class DataValidation:
    """
    This class handles the validation of ingested data by ensuring the required files
    are present in the specified feature store directory.
    """
    
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig
        ):
        """
        Constructor for the DataValidation class.

        :param data_ingestion_artifact: Contains paths to the ingested data artifacts.
        :param data_validation_config: Configuration for data validation, including required files and directories.
        """
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise AppException(e, sys)
        
        
    def validate_all_files_exist(self) -> bool:
        """
        Validates if all the required files exist in the feature store directory.

        :return: Boolean indicating whether validation was successful or not.
        :raises AppException: If an error occurs during the validation process.
        """
        try:
            validation_status = None
            
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        
            return validation_status
            
        except Exception as e:
            raise AppException(e, sys)
        
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        Orchestrates the data validation process by checking the presence of required files.

        :return: DataValidationArtifact containing the validation status.
        :raises AppException: If an error occurs during the validation process.
        """
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status=status
            )
            
            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data Validation artifact: {data_validation_artifact}")
            
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
                
            return data_validation_artifact
        
        except Exception as e:
            raise AppException(e, sys)