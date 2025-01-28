from fastapi import FastAPI
from graphene import Field, Int, List, ObjectType, String, Schema
from starlette_graphene3 import (
    GraphQLApp,
    make_graphiql_handler,
    make_playground_handler,
)
from BackendApi.data.data import employers_data, jobs_data


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
