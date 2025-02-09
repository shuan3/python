from pymongo import MongoClient

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
DB_NAME = "graphql"
COLLECTION_NAME = "employers"

# @app.route("/")
# def getDatas():
#     connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
#     collection = connection[DB_NAME][COLLECTION_NAME]
#     projects = collection.find()
#     json_projects = []
#     for project in projects:
#         json_projects.append(project)
#     json_projects = json.dumps(json_projects, default=json_util.default)
#     connection.close()
#     return json_projects

# getDatas()
def update_data(data, collection_name):
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DB_NAME][collection_name]
    if data["employer_id"]:
        collection.delete_one({"employer_id": data["employer_id"]})
        collection.insert_one(data)
    connection.close()
    print(f"Updated {data['employer_id']} records in {collection_name}")


def insert_data(data, collection_name):
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DB_NAME][collection_name]
    collection.delete_many({})
    collection.insert_many(data)
    connection.close()
    print(f"Inserted {len(data)} records into {collection_name}")


# connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
# db = connection['graphql']
# employers_collection = db['employers']
# jobs_collection = db['jobs']

# employers_collection.insert_many(employers_data)
# jobs_collection.insert_many(jobs_data)

# print("done")
