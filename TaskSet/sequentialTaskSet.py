from locust import HttpUser, task, constant, SequentialTaskSet

class MySeqTask(SequentialTaskSet):
  
  @task
  def get_status(self):
    self.client.get("/200")
    print("Get Status of 200")

  @task
  def get_500_status(self):
    self.client.get("/500")
    print("Get Status of 500")

class MyLoadTest(HttpUser):
  host = "https://http.cat"
  tasks = [MySeqTask]
  wait_time = constant(1)
