print("Content-type application/json")
print("")

import json, random
obj = None
with open("example.json", "r") as file:
    obj = json.load(file)

obj['temperature'] = random.randint(-15, 30)
obj['humidity'] = random.randint(40, 100)
obj['meter']['electricity']['reading'] = round(random.uniform(12345.9, 12347.9),3)
obj['meter']['electricity']['consumption'] = round(random.uniform(0.1, 2.0),1)
obj['meter']['gas']['reading'] = round(random.uniform(2367.9, 2369.9),3)
obj['meter']['gas']['consumption'] = round(random.random(),1)
obj['meter']['water']['reading'] = round(random.uniform(1212.9, 1214.9),3)
obj['meter']['water']['consumption'] = round(random.uniform(0.1, 1.0),1)
# obj['boiler']['isRun'] = random.choice([True, False])
obj['boiler']['temperature'] = random.randint(60, 65)
obj['boiler']['pressure'] = round(random.uniform(1.0, 2.0),1)

print(json.dumps(obj))


