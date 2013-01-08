from datetime import timedelta
from random import randint
from datetime import date
from datetime import time
from datetime import datetime
import csv


def random_date(start, end):
    return start + timedelta(
        seconds=randint(0, int((end - start).total_seconds())))

def get_emails(fname):
    emails = []
    f = open(fname, 'r')
    try:
        reader = csv.reader(f)
        for row in reader:
            email = str.lower(row[0] + "_" + row[1]) + "@tester.com"
            emails.append(email);
    finally:
        f.close()
    return emails
    
def get_comments(fname):
  comments = [line.strip() for line in open(fname)] 
  return comments

 

def create_message():
    names_len = names.__len__()-1
    comments_length=comments.__len__()-1
    body_line_id = randint(0,comments_length)
    #print body_line_id
    msg = {"from": names[randint(0, names_len)],
        "to": [ names[randint(0, names_len)], names[randint(0, names_len)], names[randint(0, names_len)] ],
        "sent": dt,
        "body": comments[randint(0,comments_length )] }
    return msg


d1 = date(2006, 12, 31)
d2 = date(2013, 01, 05)
names = tuple(get_emails("randomNames.csv"))
comments = tuple(get_comments("comments.txt"))
dt =  datetime.combine(random_date(d1, d2), time.min)

