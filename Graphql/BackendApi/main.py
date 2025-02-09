from fastapi import FastAPI
from graphene import Field, Int, List, ObjectType, String, Schema
from starlette_graphene3 import (
    GraphQLApp,
    make_graphiql_handler,
    make_playground_handler,
)
from BackendApi.data.data import employers_data, jobs_data
from pymongo import MongoClient
from BackendApi.mongodb import (
    MONGODB_HOST,
    MONGODB_PORT,
    DB_NAME,
    insert_data,
)
from BackendApi.app.gql.types import EmployerObject, JobObject
from BackendApi.app.gql.mutation import Mutation
from BackendApi.app.gql.query import Query


schema = Schema(query=Query, mutation=Mutation)


app = FastAPI()
app.mount(
    "/graphql",
    GraphQLApp(schema=schema, on_get=make_graphiql_handler()),
)
app.mount(
    "/graphql-p",
    GraphQLApp(schema=schema, on_get=make_playground_handler()),
)

# @app.post("/get_employers/")
# def get_employers():
#     connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
#     collection = connection[DB_NAME]["employers"]
#     projects = collection.find()
#     json_projects = []
#     for project in projects:
#         json_projects.append(project)
#     json_projects = json.dumps(json_projects)
#     connection.close()
#     return json_projects


@app.get("/employers/")
async def get_employers():

    insert_data(employers_data, "employers")
    employers = []
    for employer in MongoClient(MONGODB_HOST, MONGODB_PORT)[DB_NAME][
        "employers"
    ].find():
        employers.append(
            {
                "id": str(employer["_id"]),
                "name": employer["name"],
                "contact_email": employer["contact_email"],
                "industry": employer["industry"],
            }
        )
    return employers


@app.get("/jobs/")
async def get_jobs():
    insert_data(jobs_data, "jobs")
    jobs = []
    for job in MongoClient(MONGODB_HOST, MONGODB_PORT)[DB_NAME]["jobs"].find():
        jobs.append(
            {
                "id": str(job["_id"]),
                "title": job["title"],
                "description": job["description"],
                "employer_id": job["employer_id"],
            }
        )
    return jobs


# mongodb://localhost:27017/
