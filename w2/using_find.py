import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
scores = db.scores

try:
    doc = scores.find_one()
except:
    print "Unexpected error:", sys.exc_info()[0]


print doc

