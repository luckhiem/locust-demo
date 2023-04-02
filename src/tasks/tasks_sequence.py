from locust import HttpUser, task, SequentialTaskSet


class TasksSequence(SequentialTaskSet):
    @task
    def task_1(self):
        print('Running index - 1')
        self.client.get("/projects")

    @task
    def task_2(self):
        print('Running index - 2')
        self.client.get("/tasks")


class LoadUserTaskSet(HttpUser):
    host = "https://api.todoist.com/rest/v2"
    tasks = [TasksSequence]
