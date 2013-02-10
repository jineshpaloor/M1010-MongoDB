import pymongo
import sys

#establish connection with database
connection = pymongo.Connection("mongodb://localhost", safe=True)

#get handle for students database
db=connection.students
grades=db.grades

def remove_lowest_score():
    print 'removing lowest score'

