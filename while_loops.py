# TODO: Define the budget for the cultural tour
cultural_tour_budget = 1500 
# TODO: Define the cost associated with each city visit
city_costs = {"New York":300, "Chicago":500,"Texas":280,"San Francisco": 300,"Miami":250}
# TODO: Initialize the total amount spent and the list of chosen cities
total_spent = 0
selected_cities = []
# TODO: Use a while loop to selectively add cities to the tour list based on the budget
# Inside the loop:
    # TODO: Retrieve a city and its associated cost
    # TODO: Check if adding this city would exceed your budget
        # TODO: If not, update the total spent and add the city to your list
while total_spent < cultural_tour_budget and city_costs:
    city,cost = city_costs.popitem()
    if total_spent + cost <= cultural_tour_budget:
        total_spent += cost
        selected_cities.append(city)

# TODO: Print the list of cities chosen for the cultural tour
print("The list of the cities:", selected_cities)