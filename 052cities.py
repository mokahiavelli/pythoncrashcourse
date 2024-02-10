def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Example usage:
location1 = city_country("santiago", "chile")
location2 = city_country("tokyo", "japan")
location3 = city_country("paris", "france")

print(location1)
print(location2)
print(location3)
