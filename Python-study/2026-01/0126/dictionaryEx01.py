capitals = {"Korea": "Seoul", "USA": "Washington", "UK": "London"}

for key in capitals:
    print(capitals[key])

for k in capitals.keys():
    print(k)

for v in capitals.values():
    print(v)

capitals = {"Korea": "Seoul", "USA": "Washington", "UK": "London"}
for k, v in capitals.items():
    print(k, v)
