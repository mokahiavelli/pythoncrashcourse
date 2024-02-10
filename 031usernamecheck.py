current_users = ['brian', 'bob', 'admin', 'ye', 'king']
new_users = ['paul', 'ringo', 'john', 'george', 'brian']

lc_current_users = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in lc_current_users:
        print("You must select a new username.")
    else: print("Your username is available.")