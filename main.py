
from MLOps_Project import logger
from MLOps_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLOps_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLOps_Project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MLOps_Project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME  = "Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    



STAGE_NAME = "Data Validation Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
            
            
STAGE_NAME = "Data Transformation Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e            
    

STAGE_NAME = "Model Trainer Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e        