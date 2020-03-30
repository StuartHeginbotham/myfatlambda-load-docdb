import logging
import sys
import boto3
import pymongo
import json

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
                    
try:
    mycluster=sys.argv[1]    #connection string for DocumentDB cluster
    mydb=sys.argv[2]         #database - will be created if it does not exist
    mycollection=sys.argv[3] #collection - will be create if it does not exist
    
    logging.info(f'DocumentDB --- cluster: {sys.argv[1]}, database: {sys.argv[2]}, collection: {sys.argv[3]}')
except:
    logging.error(f'Input file and bucket not specified correctly')
    
client = pymongo.MongoClient(mycluster)

# Define connection to Document DB collection

db=client.mydb
col=db.mycollection

for doc in col.find():
    logging.info(f'document: {doc}')

