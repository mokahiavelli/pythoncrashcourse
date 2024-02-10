my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 

my_foods.append('cannoli') 
friend_foods.append('ice cream') 

print("My favorite foods are:")

for myfood in my_foods:
    print(myfood)

print("\nMy friend's favorite foods are:")

for friendfoods in friend_foods:
    print(friendfoods)
