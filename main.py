import json

# Load JSON data from a file
with open("free.json", "r") as file:
    data = json.load(file)

# Loop through each record and print the `classSchedule` if it exists
for record in data:
    if "classSchedule" in record:
        print(record["classSchedule"])

