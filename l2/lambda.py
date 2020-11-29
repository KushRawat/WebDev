people = [
    {"name": "Cho", "house": "Gryffindor"},
    {"name": "Harry", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# def f(person):
    # return person["name"]
    # return person["house"]

# people.sort(key = f)

people.sort(key = lambda person: person["name"])

print(people)