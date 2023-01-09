import threading
import time
import json, requests

def task2():
    response = requests.get("http://localhost:8000/cgi-bin/rest.py")
    print(response.text)

    # json_w = json.loads(response.text)
    # temp = json_w['temperature']
    # print(f"🌡 Текущая температура {temp} ℃")


th2 = threading.Thread(target=task2)

timer = threading.Timer(3, task2)
timer.start()

th2.start()
th2.join()

