import threading
import time
import json, requests
import sys

json_w = ""

lock_json_w = threading.Lock()
exit_event = threading.Event()

print("""
    Меню:
1. Температура/Влажность
    1.1 Текущая # последняя запись в файле
    1.2 Средняя # среднее 6 последних записей
2. Счетчики
    2.1 Электроенергия # показания счетчика, текущий расход
    2.2 Газ # показания счетчика, текущий расход
    2.3 Вода # показания счетчика, текущий расход
3. Котел
   3.1 Состояние # Включен/Выключен, температура, давление
   3.2 Включить # Команда на включение
   3.3 Выключить # Команда на выключение
4. Журнал # все записи из файла
      """)

def menu():
    choice = input('Select a menu item: ')
    if choice == "1.1":
        lock_json_w.acquire()
        temp = json_w['temperature']
        lock_json_w.release()
        print(f"🌡 Текущая температура {temp} ℃")
    elif choice == "2.1":
        lock_json_w.acquire()
        electricity = json_w['meter']['electricity']
        lock_json_w.release()
        print(f"Счетсик електроенергии {electricity}")
    elif choice == "2.2":
        lock_json_w.acquire()
        gas = json_w['meter']['gas']
        lock_json_w.release()
        print(f"Счетчик газа {gas}")
    elif choice == "2.3":
        water = json_w['meter']['gas']
        print(f"Счетчик водьі {water}")
    elif choice == "3.1":
        lock_json_w.acquire()
        boiler = json_w['boiler']
        lock_json_w.release()
        print(f"Состояние бойлера {boiler}")
    elif choice == "3.2":
        pass
    elif choice == "3.3":
        pass
    elif choice == "4":
        pass
    exit_event.set()
    sys.exit()


def req():
    global json_w
    while True:
        if exit_event.is_set():
            return
        response = requests.get("http://localhost:8000/cgi-bin/rest.py")
        # print(response.text)
        lock_json_w.acquire()
        json_w = json.loads(response.text)
        lock_json_w.release()
        time.sleep(5)
    # return json_w


th1 = threading.Thread(target=menu)
th2 = threading.Thread(target=req, daemon=True)

th1.start()
th2.start()
# th2.setDaemon(True)
# timer = threading.Timer(5, req)
# timer.start()

th1.join()
th2.join()

