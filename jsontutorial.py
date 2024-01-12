# Converting python to json and vice versa- Serialisation,Encode & Deserialization,Decode
import json

employee = {"name": "adam", "age": "30", "city": "newyork", "id": 120, "role": ["qa", "engineer"],
            "ismarried": True}  # dictionary
print(employee)

ejson = json.dumps(employee, indent=4, sort_keys=True)
print(ejson)

with open('employee.json', 'w') as file:  # save json into file
    json.dump(employee, file, indent=4)

edict = json.loads(ejson)  # converting json to python dictionary
print(edict)

with open('employee.json', 'r') as file:  # loading json from file
    edictfile = json.load(file)
    print(edictfile)


# Custom class objects
# Encoding
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Tom", 25)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userjson = json.dumps(user, default=encode_user)
print(userjson)


# Decoding
def decode_user(dicto):
    if User.__name__ in dicto:
        return User(name=dicto['name'], age=dicto['age'])
    return dicto


userdicto = json.loads(userjson, object_hook=decode_user)
print(user.name)
