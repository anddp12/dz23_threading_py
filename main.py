import threading
import time
import json, requests

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

choice = input('Select a menu item: ')
if choice == "1":
    pass
elif choice == "2":
    pass
elif choice == "2.1":
    pass
elif choice == "2.2":
    pass
elif choice == "2.3":
    pass
elif choice == "3":
    pass
elif choice == "3.1":
    pass
elif choice == "3.2":
    pass
elif choice == "3.3":
    pass


def task2():
    response = requests.get("http://localhost:8000/cgi-bin/rest.py")
    print(response.text)

#     # json_w = json.loads(response.text)
#     # temp = json_w['temperature']
#     # print(f"🌡 Текущая температура {temp} ℃")


th2 = threading.Thread(target=task2)

timer = threading.Timer(5, task2)
timer.start()

th2.start()
th2.join()

