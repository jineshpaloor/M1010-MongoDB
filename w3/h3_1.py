import pymongo
import sys

"""
find the lowest homework in code and then update the scores array with the low homework pruned.
If you are struggling with the Python side of this, look at the remove operator,
which can remove stuff from a Python list.
{ "_id" : 0, "name" : "aimee Zank", "scores" : [
            { "type" : "exam", "score" : 1.463179736705023 },
            { "type" : "quiz", "score" : 11.78273309957772 },
            { "type" : "homework", "score" : 6.676176060654615 },
            { "type" : "homework", "score" : 35.8740349954354 } ]
}
"""
# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students= db.students


def drop_low_score_homework():

    print "dropping low score homework"


    try:
        query = {'scores.type':{'$in':['homework']}}
        cursor = students.find(query)

        for doc in cursor:
            hw_dict = []
            for s in doc['scores']:
                if s['type'] == 'homework':
                    hw_dict.append(s)
            sorted_hw_dict = sorted(hw_dict, key=lambda k: k['score'])
            doc['scores'].remove(sorted_hw_dict[0])
            students.update({'_id':doc['_id']},{'$set':{'scores':doc['scores']}})
    except:
        print "Unexpected error:", sys.exc_info()[0]


drop_low_score_homework()

