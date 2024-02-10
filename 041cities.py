cities = {
    'New York': {
        'country': 'United States',
        'population': '8.4 million',
        'fact': 'The Statue of Liberty is located in New York Harbor.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Tokyo is the most populous metropolitan area in the world.'
    },
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'The Eiffel Tower was completed in 1889 and stands 324 meters tall.'
    }
}

for city, info in cities.items():
    print(f"\n{city}:")
    for category, data in info.items():
        print(f"{category.capitalize()}: {data}")
