from locust import TaskSet, constant, task, HttpUser
import random

class MyHTTPCat(TaskSet):

  @task
  def get_status(self):
    self.client.get("/200")
    print("Get Status of 200")

  @task
  def get_random_status(self):
    status_code = ["100", "101", "200", "201", "202", "204", "206", "207", "300", "301", "302", "303", "304", "305", "307", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "420", "421", "422", "423", "424", "425", "426", "429", "431", "444", "450", "451", "500", "501", "502", "503", "504", "506", "507", "508"]
    random_url = "/" + str(random.choice(status_code))
    res = self.client.get(random_url)
    print("Random Http Status")
    


class MyLoadTest(HttpUser):
  host = "https://http.cat"
  tasks = [MyHTTPCat]
  wait_time = constant(1)

