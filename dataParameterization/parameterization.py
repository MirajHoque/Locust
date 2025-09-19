from locust import HttpUser, task, constant, SequentialTaskSet
from readTestData import CsvRead

class MyScript(SequentialTaskSet):
    @task
    def placeOrder(self):
        testData = CsvRead("dataParameterization/customer-data.csv").read()
        print(testData)

        data = {
            "custname" : testData['name'],
            "custtel": testData['phone'],
            "custemail": testData['email'],
            "size": testData['size'],
            "topping": testData['toppings'],
            "delivery": testData['time'],
            "comments": testData['instructions']
        }

        name = "Order for" + testData['name']

        with self.client.post("/post", catch_response=True, name=name, data=data) as response:
            if response.status_code == 200 and testData['name'] in response.text:
                response.success()
            else:
                response.failure("Failure in processing the order")

class MyLoadTest(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [MyScript]
                
