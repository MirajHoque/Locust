from locust import User, task, constant

class MyFirstTest(User):
  weight = 2 # load(user) distribution
  wait_time = constant(1) #wait time between tasks

  @task
  def launch(self):
    print("Launching the URL")

  @task #decorator
  def search(self):
    print("searching")

class MySecondTest(User):
  weight = 2
  wait_time = constant(1)
  @task
  def launch2(self):
    print("Launching the URL from second class")

  @task
  def search2(self):
    print("searching from second class")
  