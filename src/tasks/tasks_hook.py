from locust import HttpUser, between, task, events


@events.test_start.add_listener
def script_start():
    """Fired on each node when a new load test is started. It's not fired again if the number of
    users change during a test."""
    print('Test Start')


@events.test_stop.add_listener
def script_stop():
    """Fired on each node when a load test is stopped."""
    print('Test Stop')


class LoadUser(HttpUser):
    wait_time = between(1, 3)

    host = "https://google.com"

    def on_start(self):
        print('Start Hook')

    @task
    def index_1(self):
        print('Running index 1')
        self.client.get("/")

    def on_stop(self):
        print('Stop Hook')
