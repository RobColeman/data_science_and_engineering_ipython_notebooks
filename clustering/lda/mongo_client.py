# mongo_client.py
import pymongo
from bson import ObjectId
from pymongo import MongoClient

mongo_ip = "omitted"
mongo_port = "omitted"
mongo_db_name = "omitted"
event_collection_name = "event_types"
session_collection_name = "sessions"

def get_events_ids_by_project_id(project_id):
    # project_id string 
    query = { 'project_id' : ObjectId(project_id) }
    fields = { '_id': 1 }
    event_types_collection = MongoClient(mongo_ip, mongo_port)[mongo_db_name][event_collection_name]
    cursor = event_types_collection.find(query,fields)
    return [str(et_id['_id']) for et_id in cursor]


def get_sessions_batch(project_id, n_skip = 0, n_limit = -1):
    query = { 'instance_id' : project_id }
    fields = { '_id': 0, 'event_count': 1 }
    sessions_collection = MongoClient(mongo_ip, mongo_port)[mongo_db_name][session_collection_name]
    cursor = sessions_collection.find(query,fields)
    if n_limit > 0:
        output = [to_session_events_array(s['event_count']) for s in cursor.skip(n_skip).limit(n_limit)]
    else:
        output = [to_session_events_array(s['event_count']) for s in cursor.skip(n_skip)]
    return output


def get_session_count(project_id):
    query = { 'instance_id' : project_id }
    sessions_collection = MongoClient(mongo_ip, mongo_port)[mongo_db_name][session_collection_name]
    cursor = sessions_collection.find(query)
    return cursor.count()


def to_session_events_array(event_count_dict):
    output = []
    for k, v in event_count_dict.items():
        output.extend([k]*v) ## flatten
    return output


def build_batches(n, batch_size):
    for n_skip in xrange(0,n,batch_size):
        if n_skip >= (n - batch_size):
            n_limit = -1
        else:
            n_limit = batch_size
        yield (n_skip, n_limit)

