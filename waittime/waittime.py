from locust import User, task, constant, constant_pacing, between
import time

class MyUser(User):
  wait_time = constant_pacing(3)

  @task
  def launch(self):
    time.sleep(5)
    print("Constant pacing demo")
