from fastapi import FastAPI
from graphene import Field, Int, List, ObjectType, String, Schema
from starlette_graphene3 import (
    GraphQLApp,
    make_graphiql_handler,
    make_playground_handler,
)
from BackendApi.data.data import employers_data, jobs_data

# from pymongo import MongoClient
from BackendApi.mongodb import (
    MONGODB_HOST,
    MONGODB_PORT,
    DB_NAME,
    insert_data,
)
from BackendApi.app.gql.types import EmployerObject, JobObject

# from BackendApi.app.gql.mutation import Mutation


class Query(ObjectType):
    # employers=List(lambda: EmpployerObject)
    # jobs=List(lambda: JobObject)
    employers = List(EmployerObject)
    jobs = List(JobObject)

    def resolve_employers(self, info):
        return employers_data

    def resolve_jobs(self, info):
        return jobs_data
