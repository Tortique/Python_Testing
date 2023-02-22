from locust import HttpUser, task


class PerfTest(HttpUser):

    @task
    def home(self):
        self.client.get('http://127.0.0.1:5000/')

    @task
    def points_recap(self):
        self.client.get('http://127.0.0.1:5000/pointsRecap')

    @task
    def login(self):
        self.client.post('http://127.0.0.1:5000/showSummary', {'email': 'john@simplylift.co'})

    @task
    def booking(self):
        self.client.get('http://127.0.0.1:5000/book/Spring%20Festival/Simply%20Lift')

    @task
    def purchase(self):
        self.client.post('http://127.0.0.1:5000/purchasePlaces', {'club': 'Simply Lift',
                                                                  'competition': 'Spring Festival',
                                                                  'places': '1'})

    @task
    def logout(self):
        self.client.get('http://127.0.0.1:5000/logout')
