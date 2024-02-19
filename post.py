from locust import HttpUser, task, between
import json

class Post(HttpUser):
    wait_time = between(1, 3)  # Time between consecutive requests
    host = 'https://northamerica-northeast1-arquisoft4019.cloudfunctions.net'

    @task
    def my_post_task(self):
        # Define your POST request payload
        payload = {
            "key1": "value1",
            "key2": "value2"
        }
        
        
        # Message to be published
        message = '{"placa": "ABC123","timestamp": "2022-07-01T12:00:00Z","latitude": 4.710989,"longitude": -74.072092,"velocity": 60,"direction": "Norte","temperature": 25}'
        message_json = json.loads(message)

        # Send the POST request
        response = self.client.post("/sendsignal", json=message_json)
        

        # Print the response status code and content (optional)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")

