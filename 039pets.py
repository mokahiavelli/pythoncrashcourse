pet1 = {
    "name": "Tony",
    "kind": "Dog",
    "owner": "John"
}

pet2 = {
    "name": "Geezer",
    "kind": "Cat",
    "owner": "Alice"
}

pet3 = {
    "name": "Ozzy",
    "kind": "Rabbit",
    "owner": "Bob"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Pet Name: {pet['name']}")
    print(f"Kind: {pet['kind']}")
    print(f"Owner: {pet['owner']}")
    print("\n")
