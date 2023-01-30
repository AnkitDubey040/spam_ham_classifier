import pandas as pd
from data_dump import mongo_client,DATABASE_NAME ,COLLECTION_NAME
import os,sys 
import json
import numpy as np

# to get mongo data as a pandas dataframe : 

def get_collection_as_dataframe(database_name:str , collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """

    df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
    if "_id" in df.columns:
        df = df.drop("_id",axis=1)
    return df
df = get_collection_as_dataframe(database_name=DATABASE_NAME, collection_name = COLLECTION_NAME)
print(df)
df.to_csv("sapm_ham.csv", index=False)