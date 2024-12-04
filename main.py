import json

# File path to the JSON file
input_file = "output.json"

# Open and load the JSON data
with open(input_file, "r") as infile:
    json_data = json.load(infile)

# Use a set to collect unique room numbers
unique_room_numbers = set()

# Add room numbers to the set (avoids duplicates)
for item in json_data:
    unique_room_numbers.add(item["roomNumber"])

# Convert the set to a list
room_numbers_list = list(unique_room_numbers)

# Print the unique list of room numbers
print(room_numbers_list)
