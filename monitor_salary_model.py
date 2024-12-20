import requests, time
def monitor_salary_model():
    URL = "http://127.0.0.1:5000/predict/-70"
    while True:
        print(requests.get(URL).text)
        time.sleep(1)

monitor_salary_model()