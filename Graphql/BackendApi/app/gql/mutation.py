from graphene import Mutation, ObjectType, String, Int, Field
from BackendApi.main import JobObject
from BackendApi.data.data import employers_data, jobs_data
from pymongo import MongoClient
from BackendApi.mongodb import (
    MONGODB_HOST,
    MONGODB_PORT,
    DB_NAME,
    insert_data,
    update_data,
)


class AddJob(Mutation):
    class Arguments:
        title = String()
        description = String()
        employer_id = Int()

    job = Field(lambda: JobObject)

    def mutate(self, info, title, description, employer_id):
        job = {
            "id": len(jobs_data) + 1,
            "title": title,
            "description": description,
            "employer_id": employer_id,
        }
        jobs_data.append(job)
        # connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        insert_data(jobs_data, "jobs")
        return AddJob(job=job)


class UpdateJob(Mutation):
    class Arguments:
        # job_id = Int()
        title = String()
        description = String()
        employer_id = Int()

    job = Field(lambda: JobObject)

    def mutate(self, info, title, description, employer_id):
        job = {
            "id": len(jobs_data) + 10,
            "title": title,
            "description": description,
            "employer_id": employer_id,
        }

        # connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        update_data(job, "jobs")
        # job = next((job for job in jobs_data if job["id"] == job_id), None)
        # if job:
        #     job["title"] = title
        #     job["description"] = description
        #     job["employer_id"] = employer_id
        #     insert_data(jobs_data, "jobs")
        return UpdateJob(job=job)


class Mutation(ObjectType):
    add_job = AddJob.Field()
    update_job = UpdateJob.Field()
