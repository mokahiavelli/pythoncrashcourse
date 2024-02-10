pizzas = ['pepperoni', 'aubergine', 'four cheese', 'vegtable']
yrpizzas = pizzas
pizzas.append('seafood')
for pizza in pizzas:
    print("I really like " +pizza.title())
yrpizzas.append('mushroom')
for yrpizza in yrpizzas:
    print("My friend really likes " +yrpizza.title())