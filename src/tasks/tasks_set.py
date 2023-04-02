from locust import HttpUser, between, task, TaskSet
from src.common.auth import BEARER_TOKEN
from src.common.config import HOST


class StoreTaskSet(TaskSet):

    @task(1)
    def task_1(self):
        print('Running index - 1')
        self.client.get("/projects", name="task_1", headers={"Authorization": "Bearer " + BEARER_TOKEN})

    @task(3)
    def task_2(self):
        print('Running index - 2')
        self.client.get("/tasks", name="task_2", headers={"Authorization": "Bearer " + BEARER_TOKEN})

    @task(2)
    def task_3(self):
        print('Running index - 3')
        with self.client.get("/tasks", name="task_3", catch_response=True) as response:
            if response.status_code == 401:
                response.success()


class LoadUserTaskSet(HttpUser):
    wait_time = between(1, 3)
    host = HOST
    tasks = [StoreTaskSet]
