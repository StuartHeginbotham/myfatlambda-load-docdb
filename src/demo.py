import logging
import sys
import boto3
import pymongo
import json

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

logging.info('Fat Lambda Params ****STARTED****')

# Receive file name via the first argument on the command line
try:
    mybucket=sys.argv[1]    #bucket name
    mykey=sys.argv[2]       #key name for file
    mycluster=sys.argv[3]    #connection string for DocumentDB cluster
    mydb=sys.argv[4]         #database - will be created if it does not exist
    mycollection=sys.argv[5] #collection - will be create if it does not exist
    
    logging.info(f'S3 --- bucket: {sys.argv[1]}, key: {sys.argv[2]}')
    logging.info(f'DocumentDB --- cluster: {sys.argv[3]}, database: {sys.argv[4]}, collection: {sys.argv[5]}')
except:
    logging.error(f'Input file and bucket not specified correctly')


s3=boto3.resource('s3')
client = pymongo.MongoClient(mycluster)

# Connect with s3 object

try:
    obj=s3.Object(mybucket,mykey)
except:
    logging.error(f'Failed to access bucket and or file')

# Retrieve body from s3 object

try:  
    mybody=obj.get()['Body'].read().decode("utf-8").splitlines()
    logging.info(f'mybody: {mybody}')
except:
    logging.error(f'Failed to retrieve body of input')

# Define connection to Document DB collection

db=client.mydb
col=db.mycollection

# Retrieve line from s3 object body and write it to documentDB as a document

for line in mybody:
    try:
        logging.info(f'line: {line}')
        col.insert_one(json.loads(line))
    except Exception as e:
        logging.error(f'Failed on retrieve and insert, line: {line}, {e}')

