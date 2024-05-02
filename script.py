import random
from datetime import datetime, timedelta
from itertools import combinations

# Sample data for colleges and sports
colleges = [
    {"id": 1, "name": "Benjamin Franklin"},
    {"id": 2, "name": "Berkeley"},
    {"id": 3, "name": "Branford"},
    # Add more colleges here
]

sports = [
    {"id": 1, "name": "Soccer"},
    {"id": 2, "name": "Flag Football"},
    {"id": 3, "name": "Spikeball"},
    # Add more sports here
]

# Function to generate random date and time for matches
def generate_datetime():
    start_date = datetime.now() + timedelta(days=7)  # Start from a week later
    end_date = start_date + timedelta(days=14)  # Matches for next two weeks
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    random_time = "{:02d}:{:02d}".format(random.randint(8, 20), random.randint(0, 59))  # Random time between 8am and 8pm
    return random_date.strftime("%Y-%m-%d"), random_time

# Generate matches
matches = []
for sport in sports:
    colleges_combinations = list(combinations(colleges, 2))  # Generate all possible combinations of colleges
    random.shuffle(colleges_combinations)  # Shuffle the combinations
    for college1, college2 in colleges_combinations:
        match_date, start_time = generate_datetime()
        matches.append({
            "college_id1": college1["id"],
            "college_id2": college2["id"],
            "college_pts1": -1,
            "college_pts2": -1,
            "sport_id": sport["id"],
            "location": "Lanman Center",
            "date": match_date,
            "start_time": start_time,
            "ref_id": ""  # You need to assign referees
        })

# Print generated matches
for match in matches:
    print(match)
