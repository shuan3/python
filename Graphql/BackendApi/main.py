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
    COLLECTION_NAME,
    insert_data,
)
import json


class EmployerObject(ObjectType):
    id = String()
    name = String()
    contact_email = String()
    industry = String()
    jobs = List(lambda: JobObject)

    @staticmethod
    def resolve_jobs(root, info):
        return [job for job in jobs_data if job["employer_id"] == root["id"]]


class JobObject(ObjectType):
    id = Int()
    title = String()
    description = String()
    employer_id = Int()
    employers = Field(lambda: EmployerObject)

    @staticmethod
    def resolve_employers(root, info):
        return next(
            (emp for emp in employers_data if emp["id"] == root["employer_id"]), None
        )


class Query(ObjectType):
    # employers=List(lambda: EmpployerObject)
    # jobs=List(lambda: JobObject)
    employers = List(EmployerObject)
    jobs = List(JobObject)

    def resolve_employers(self, info):
        return employers_data

    def resolve_jobs(self, info):
        return jobs_data


# class Query(ObjectType):
#     hello = String(name=String(default_value="graphql"))

#     def resolve_hello(self, info, name):
#         return f"Hello {name}"

#     tp = String(name=String(default_value="trumpp"))
#     def resolve_tp(self, info, name):
#         return f"why {name} ?"


schema = Schema(query=Query)


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
