from locust import User, constant, task, HttpUser

class MyLoadTest(HttpUser):
  wait_time = constant(1)
  @task
  def launch(self):
    self.client.get("/")