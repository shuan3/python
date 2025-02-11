import luigi


class TaskA(luigi.Task):
    def output(self):
        return luigi.LocalTarget("task_a.txt")

    def run(self):
        with self.output().open("w") as f:
            f.write("Task A completed")


class TaskB(luigi.Task):
    def requires(self):
        return TaskA()

    def output(self):
        return luigi.LocalTarget("task_b.txt")

    def run(self):
        with self.output().open("w") as f:
            f.write("Task B completed")


class TaskC(luigi.Task):
    def requires(self):
        return TaskB()

    def output(self):
        return luigi.LocalTarget("task_c.txt")

    def run(self):
        with self.output().open("w") as f:
            f.write("Task C completed")


class MainTask(luigi.Task):
    def requires(self):
        return TaskC()

    def output(self):
        return luigi.LocalTarget("main_task.txt")

    def run(self):
        with self.output().open("w") as f:
            f.write("Main Task completed")


if __name__ == "__main__":
    luigi.build([MainTask()], workers=5, local_scheduler=False)
#  print("done")
#  luigi.build([MyTask1(x=10), MyTask2(x=15, z=3)])
