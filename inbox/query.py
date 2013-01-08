#!/usr/bin/python
import time
import logging
import utils
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import pymongo
from pymongo import MongoClient




def read_inbox(name):
    begin = time.time()
    messages.find({ "to": name }).sort("sent",-1).count()  
    end = time.time()
    elapsed = end - begin
    logger.info(elapsed)
    

logger = logging.getLogger("exectime")
logger.setLevel(logging.INFO)
fh = logging.FileHandler( "query.log")
logger.addHandler(fh)

connection = MongoClient()
db = connection.test
messages = db.messages

#read_inbox("christian_cline@tester.com")
recipients = [line.strip() for line in open("recipients.log")]

for r in range(recipients.__len__()):
        #logger.info(recipients[r])
        #print recipients[r]
        read_inbox(recipients[r])
print "complete"    