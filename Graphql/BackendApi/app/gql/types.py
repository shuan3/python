from graphene import Field, Int, List, ObjectType, String, Schema
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
