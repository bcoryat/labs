#!/usr/bin/python
import time
import logging
import utils
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import pymongo
from pymongo import MongoClient


    
def save_message(msg):
    if msg.get("_id"):
       msg.pop("_id")
    begin = time.time()
    msg_id = db.messages.insert(msg) 
    end = time.time()
    elapsed = end - begin
    logger.info(elapsed)
    return msg_id



if len(sys.argv) < 2:
    num_messages = 100
else:
    num_messages = int(sys.argv[1])
  
if num_messages < 2 :
    num_messages = 1  
type ="fanOutWrite"    
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
messages = db.messages

logger.info("FOW save")
recipients = []
for i in range(num_messages):
    msg = utils.create_message()   
    for recipient in msg.get("to"):
        save_message(msg)
        if recipient not in recipients:
           recipients.append(recipient)
    for r in range(recipients.__len__()):
        recipient_logger.info(recipients[r])
  