#from sensor.pipeline.training_pipeline import start_training_pipeline
#from sensor.pipeline.batch_prediction import start_batch_prediction
from spam_ham.logger import logging
from spam_ham.exception import SensorException
import sys,os
from spam_ham.utils import get_collection_as_dataframe

if __name__=="__main__":
    try:
        get_collection_as_dataframe(database_name = "spam_ham",collection_name = "message")
     
    except Exception as e:
      raise SensorException(e,sys)