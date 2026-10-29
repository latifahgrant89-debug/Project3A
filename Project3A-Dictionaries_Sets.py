
# Project 3A - Dictionaries and Sets


# Task 1: Create the NFL and NBA dictionaries

# Create a dictionary to match each NFL team with its city.
# The team name is the key, and the city is the value.
nfl_teams = {
    "Eagles": "Philadelphia",
    "Bills": "Buffalo",
    "Dolphins": "Miami",
    "Patriots": "New England",
    "Jets": "New York"
}

# Do the same thing for the NBA teams so we can keep their
# names and cities organized in one place.
nba_teams = {
    "76ers": "Philadelphia",
    "Lakers": "Los Angeles",
    "Celtics": "Boston",
    "Bulls": "Chicago",
    "Heat": "Miami"
}


# Task 1: Create the sets

# Make a set of Pennsylvania cities that we'll use for comparisons later.
pa_cities = {"Philadelphia", "Pittsburgh", "Harrisburg", "Erie"}

# Create a larger set with those same cities plus other Mid-Atlantic cities.
# This lets us see which cities the two sets have in common.
midatlantic_cities = {
    "Philadelphia", "Pittsburgh", "Harrisburg", "Erie",
    "Baltimore", "Washington", "Newark"
}


# Task 2: Add items to the dictionaries and sets

# Add the Commanders to the NFL dictionary and connect them to Washington.
nfl_teams["Commanders"] = "Washington"

# Add the Warriors to the NBA dictionary and connect them to Golden State.
nba_teams["Warriors"] = "Golden State"

# Use add() to put Allentown into the Pennsylvania set.
# This adds the city without changing the other cities already there.
pa_cities.add("Allentown")

# Add York to the Mid-Atlantic set so it's included in our comparisons.
midatlantic_cities.add("York")


# Task 3: Find the union of the sets

# Use | to combine both sets and get every unique city from either one.
# If a city is in both sets, it only shows up once in the result.
cities_union = pa_cities | midatlantic_cities

# Print a heading so it's easy to tell which result we're looking at.
print("\nTask 3: Union of the Sets")
print(cities_union)


# Task 4: Find the intersection of the sets

# Use & to find the cities that both sets have in common.
# Basically, we're checking which cities show up in both places.
cities_intersection = pa_cities & midatlantic_cities

# Print the heading and the cities that match in both sets.
print("\nTask 4: Intersection of the Sets")
print(cities_intersection)


# Task 5: Loop through each dictionary and print its items

# Print a heading before showing the NFL teams.
print("\nTask 5: NFL Teams")

# Use a for loop to go through the NFL dictionary one team at a time.
# items() gives us both the team name and its city in each loop.
for team, city in nfl_teams.items():

    # Print the team and city together so the information is easy to read.
    print(team, "-", city)

# Print a heading before showing the NBA teams.
print("\nNBA Teams")

# Repeat the same process for the NBA dictionary.
for team, city in nba_teams.items():

    # Print each NBA team with its matching city.
    print(team, "-", city)


# Task 6: Print only the keys

# Show a heading for the NFL team names.
print("\nTask 6: NFL Team Names")

# keys() gets only the team names without their city values.
print(nfl_teams.keys())

# Show a heading for the NBA team names.
print("\nNBA Team Names")

# Get and print only the NBA team names.
print(nba_teams.keys())


# Task 7: Print only the values

# Show a heading for the cities connected to the NFL teams.
print("\nTask 7: NFL Cities")

# values() gets only the cities from the NFL dictionary.
print(nfl_teams.values())

# Show a heading for the cities connected to the NBA teams.
print("\nNBA Cities")

# Get and print only the cities from the NBA dictionary.
print(nba_teams.values())


# Task 8: Merge and print the dictionaries

# Use | to combine the NFL and NBA dictionaries into one new dictionary.
# The original dictionaries stay the same, and the combined result
# gets saved in merged_teams.
merged_teams = nfl_teams | nba_teams

# Print the combined dictionary to see all the teams together.
print("\nTask 8: Merged Dictionaries")
print(merged_teams)


# Task 9: Update one dictionary with the other

# Use update() to add the NBA entries to the existing NFL dictionary.
# This changes nfl_teams directly instead of creating a new dictionary.
# If both dictionaries had the same key, the NBA value would replace
# the old value for that key.
nfl_teams.update(nba_teams)

# Print the updated dictionary to see the changes.
print("\nTask 9: Updated NFL Dictionary")
print(nfl_teams)


# Task 10: Find the symmetric difference of the sets

# Use ^ to find cities that are in one set but not in both.
# This gives us the cities that don't overlap between the two sets.
cities_difference = pa_cities ^ midatlantic_cities

# Print the cities that appear in only one of the sets.
print("\nTask 10: Symmetric Difference")
print(cities_difference)


# Task 11: Check the subset and superset

# Print a heading before checking how the two sets compare.
print("\nTask 11: Subset and Superset Checks")

# Use <= to check if every city in pa_cities is also in midatlantic_cities.
# The result will be False because Allentown is only in pa_cities.
print("Is pa_cities a subset of midatlantic_cities?")
print(pa_cities <= midatlantic_cities)

# Use >= to check if midatlantic_cities contains every city in pa_cities.
# This will also be False because Allentown is missing from that set.
print("Is midatlantic_cities a superset of pa_cities?")
print(midatlantic_cities >= pa_cities)
