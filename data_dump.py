import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
mongo_client = pymongo.MongoClient("mongodb+srv://ankitdubey:ankitdubey04@cluster0.ictsq1s.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "/config/workspace/spam.csv"
DATABASE_NAME = "spam_ham"
COLLECTION_NAME = "messages"

if __name__ =="__main__":
    df = pd.read_csv(DATA_FILE_PATH, encoding="latin-1")
    print(f"Rows and Columns: {df.shape}")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    df['label'] = df['type'].map({'ham': 0, 'spam': 1})
    print(f"After Cleanning the Rows and Columns are: {df.shape}")
    # convert data into json
    df.reset_index(drop = True,inplace = True)
    
    json_record = list(json.loads(df.T.to_json()).values())
    # to print a specific record
    print(json_record[0])

    # mongo_client = pymongo.MongoClient(MONGO_DB_URL)

    # input json data into mongo database:
    #mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    #print("Entered records into Mongo Db Database")
        # inpuy json data into mongo database:
    for record in json_record:
        mongo_client[DATABASE_NAME][COLLECTION_NAME].update_one({'text': record['text']}, {"$set": record}, upsert=True)
    print("Data entered into MongoDb Database")

