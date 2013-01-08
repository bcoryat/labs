#!/usr/bin/python
import time
import logging
import utils
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import pymongo
from pymongo import MongoClient



if len(sys.argv) < 2:
    num_messages = 100
else:
    num_messages = int(sys.argv[1])
    
type ="bucketedFanOutRead"    
logger = logging.getLogger("exectime")
logger.setLevel(logging.INFO)
fh = logging.FileHandler( type + "_" + "insert.log")
logger.addHandler(fh)

recipient_logger = logging.getLogger("recipients")
recipient_logger.setLevel(logging.INFO)
fh2 = logging.FileHandler(type+'recipients.log')
recipient_logger.addHandler(fh2)


connection = MongoClient()
db = connection.test

logger.info("BFOW save")
recipients = []
for i in range(num_messages):
    msg = utils.create_message() 
    for recipient in msg.get("to"):
        # Add Timing? 
       sequence = (db.users.find_and_modify(query={'user_name':recipient},update={'$inc':{'msg_count':1}},upsert=True,new=True)).get("msg_count")/50
       db.inbox.update({'owner': recipient, "sequence": sequence}, { '$push': { 'messages': msg } }, upsert=True)
       if recipient not in recipients:
           recipients.append(recipient)
    for r in range(recipients.__len__()):
        recipient_logger.info(recipients[r])