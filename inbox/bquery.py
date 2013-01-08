#!/usr/bin/python
import time
import logging
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import pymongo
from pymongo import MongoClient





def read_inbox(name):
    begin = time.time()
    inbox.find({ "owner": name }).sort("sequence",-1).count()  
    end = time.time()
    elapsed = end - begin
    logger.info(elapsed)
    

logger = logging.getLogger("exectime")
logger.setLevel(logging.INFO)
fh = logging.FileHandler( "bquery.log")
logger.addHandler(fh)

connection = MongoClient()
db = connection.test
inbox = db.inbox

#read_inbox("christian_cline@tester.com")
recipients = [line.strip() for line in open("brecipients.log")]

for r in range(recipients.__len__()):
        #logger.info(recipients[r])
        #print recipients[r]
        read_inbox(recipients[r])
print "complete" 