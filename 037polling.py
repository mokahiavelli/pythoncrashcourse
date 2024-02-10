# favourite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print(f"\n")

# 6-6
voters = ["jen", "sarah", "edward", "phil", "brian", "adrian", "kenneth", "barak"]

for user in voters:
    if user.lower() in favorite_languages.keys():
        print(f"Thank you {user} for responding to the poll")
    else:
        print(f"{user.title()}, please take the poll")