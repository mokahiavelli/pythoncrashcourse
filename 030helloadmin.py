users = ['brian', 'bob', 'admin', 'ye', 'jesus']
#line below prints if list above is empty!
if not users:
    print("We need to find some users!")
for user in users:
    if user == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else: print("Hello " + user + ", thank you for logging-in again.")
