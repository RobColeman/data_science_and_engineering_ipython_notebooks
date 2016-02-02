import re
import json
count=0
with open('movies.csv','rb') as csv_file:
    header = csv_file.readline()
    for line in csv_file.readlines():
        fixed = line.replace("\r\n","").split(",")
        if len(fixed)==3:
            title = re.sub(" \(.*\)$", "", re.sub('"','', fixed[1]))
            genre = fixed[2].split('|')
            print '{ "create" : { "_index" : "movielens", "_type" : "film", "_id" : "%s" } }' %  fixed[0]
            print'{ "id": "%s", "title" : "%s", "year":"%s" , "genre":%s }' % (fixed[0],title, fixed[1][-5:-1], json.dumps(genre))