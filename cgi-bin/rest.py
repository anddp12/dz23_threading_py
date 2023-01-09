print("Content-type application/json")
print("")

import json, random
obj = None
with open("example.json", "r") as file:
    obj = json.load(file)

obj['temperature'] = random.randint(-15, 30)

print(json.dumps(obj))


