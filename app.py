import sys
print(sys.path)

from srce.dsprojects1.logger import logging
from srce.dsprojects1.exception import CustomException
from srce.dsprojects1.components.data_ingestion import DataIngestion
from srce.dsprojects1.components.data_ingestion import DataIngestionConfig



if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)