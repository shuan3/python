# from BackendApi.data.data import employers_data, jobs_data
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

value = os.getenv("MY_VAR")
print(value)  # Output: He
