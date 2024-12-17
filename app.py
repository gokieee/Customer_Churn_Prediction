from src.SRC_CHURN.logger import logging
from src.SRC_CHURN.components.data_ingestion import DataIngestion




dataIngestion=DataIngestion()

Traindata,Testdata=dataIngestion.Initiate_DataIngestion()




logging.info("TEST")