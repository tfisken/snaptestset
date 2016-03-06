from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):

    @task(1)
    def task1(self):
#        self.client.get("oembed-web/?url=http://www.usatoday.com/story/weather/2016/01/20/winter-storm-snow-mid-atlantic-northeast/79048448/")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
