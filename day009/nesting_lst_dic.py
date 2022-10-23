'''
{
    key: [list],
    key2: {dictionary}
}
'''

# nesting
capitals = {
    "france": "paris", 
    "germany": "berlin"
}

# nesting dictionary in a list
travel_log = {
    "france": ["paris", "lille", "dijon"], 
    "germany": ["berlin", "hamburg"],
}

# nesting dictionary in a dictionary
travel_log = {
    "france": {"cities_visited": ["paris", "lille", "dijon"], 
                "total_visits": 12}, 
    "germany": ["berlin", "hamburg"],
}

# nesting dictionary in a list
travel_log = [
    {"country": "france",
     "cities_visited": ["paris", "lille", "dijon"],
     "total_visits": 12},

    {"country": "germany",
     "cities_visited": ["berlin", "hamburg"], 
     "total_visits": 5}
]

print(travel_log)