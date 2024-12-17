import sys
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from src.SRC_CHURN.exception import CustomException
from src.SRC_CHURN.logger import logging
from dataclasses import dataclass





@dataclass
class DataIngestionConfig:
    Raw_data_path:str=os.path.join("Artifact","Raw.csv")
    Train_data_path:str=os.path.join("Artifact","Train.csv")
    Test_data_path:str=os.path.join("Artifact","Test.csv")






class DataIngestion:
    def __init__(self):
        self.DataIngestionConfig=DataIngestionConfig()



    def Initiate_DataIngestion(self):
        logging.info("DataIngestionStarted")
        try:
            data=pd.read_csv("https://raw.githubusercontent.com/Vishnuu011/datastore/refs/heads/main/Telco_Customer_Churn.csv")
            logging.info("Data Has Been Loaded")
            os.makedirs(os.path.dirname(os.path.join(self.DataIngestionConfig.Raw_data_path)),exist_ok=True)
            data.to_csv(self.DataIngestionConfig.Raw_data_path,index=False)
            logging.info("Raw Data Has Been Saved In Artifact")
            train_data,test_data=train_test_split(data,test_size=0.2)
            train_data.to_csv(self.DataIngestionConfig.Train_data_path,index=False)
            test_data.to_csv(self.DataIngestionConfig.Test_data_path,index=False)
            logging.info("Test Data Has Been save In Artifact")
            logging.info("Data Ingestion Completed")
            return (
                self.DataIngestionConfig.Train_data_path,
                self.DataIngestionConfig.Test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
        


