import pymongo
import gridfs

#establish connection to database
connection = pymongo.Connection('mongodb://localhost', safe=True)

#get a handle to the schools database
db=connection.test

def main():

    grid = gridfs.GridFS(db,"videos")
    fin = open('video.mp4', 'r')

    _id = grid.put(fin)
    fin.close()

    print 'id of the files is ',_id

    videos_meta.insert({'grid_id':_id, 'filename':'video.mp4'})
