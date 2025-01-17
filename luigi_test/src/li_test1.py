import sys

# sys.path.append(r'D:\Github\test\luigi_test')
# sys.path.insert(0,'')
print(sys.path)

import luigi
from luigi import Task


class GetDBinfo:
    print("Getting DB data")
    file_name = "result.txt"


class HelloWorld(Task):
    # def requires(self):
    #     return  GetDBinfo().file_name
    def output(self):
        # print(self.input()['GetDBinfo'])
        return luigi.LocalTarget("result.txt")

    def run(self):
        print("hello")
        with self.output().open("w") as f:
            f.write("Hello world from luigi!")


# luigi.run(["HelloWorld", "--local-scheduler"])
luigi.build([HelloWorld()], workers=2, local_scheduler=False)
# if __name__ == "__main__":
#     luigi.run(["HelloWorld", "--local-scheduler"])


# https://luigi.readthedocs.io/en/stable/running_luigi.html


"""
DEBUG: Checking if HelloWorld() is complete
INFO: Informed scheduler that task   HelloWorld__99914b932b   has status   DONE
INFO: Done scheduling tasks
INFO: Running Worker with 1 processes
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
INFO: Worker Worker(salt=7614188133, workers=1, host=LAPTOP-0VCM797I, username=shanh, pid=7472) was stopped. Shutting down Keep-Alive thread
INFO:
===== Luigi Execution Summary =====

Scheduled 1 tasks of which:
* 1 complete ones were encountered:
    - 1 HelloWorld()

Did not run any tasks
This progress looks :) because there were no failed tasks or missing dependencies

===== Luigi Execution Summary =====
"""
