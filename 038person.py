person_info = {
    "first_name": "Brian",
    "last_name": "Big",
    "age": 34,
    "city": "Bradford"
}
person_info1 = {
    "first_name": "Lisa",
    "last_name": "Little",
    "age": 24,
    "city": "Leeds"
}
person_info2 = {
    "first_name": "Suzy",
    "last_name": "Small",
    "age": 45,
    "city": "Southhampton"
}

people = [person_info, person_info1, person_info2]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("\n")