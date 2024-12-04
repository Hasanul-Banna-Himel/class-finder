import json

# File path to the JSON file
input_file = "output.json"

# Open and load the JSON data
with open(input_file, "r") as infile:
    json_data = json.load(infile)

# Create a list to store all room numbers
room_numbers = [item["roomNumber"] for item in json_data]

# Print the list of room numbers
print(room_numbers)
