rubbish_teams = ['spurs', 'arsenal', 'city']
user = 'utd'

if user not in rubbish_teams:
    print(user.title() + ", You've won enough league titles to not be rubbish!")

rubbish_teams = ['spurs', 'arsenal', 'city']
user = 'spurs'

if user not in rubbish_teams:
    print(user.title() + ", You've won enough league titles to not be rubbish!")
else: print("You're a rubbish club!")
