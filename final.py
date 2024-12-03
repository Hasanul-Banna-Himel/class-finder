import json
import re

# File paths
input_file = "output.txt"
output_file = "output.json"

# List to hold JSON objects
json_data = []

# Open the input file and process each line
with open(input_file, "r") as infile:
    for line in infile:
        # Remove the "classSchedule =" prefix and strip whitespace
        schedule = line.strip().replace("classSchedule =", "").strip()
        
        # Use a regex to parse the components
        # The updated regex will allow for room numbers with dashes (e.g., 07A-07C or 08F-20C)
        match = re.match(r"(\w+)\(([\d:APM\- ]+)-([\w\-]+)\),(\w+)\(([\d:APM\- ]+)-([\w\-]+)\)", schedule)
        if match:
            class_day1, class_time1, room1, class_day2, class_time2, room2 = match.groups()
            
            # Ensure the time and room number are consistent across the schedule
            if class_time1 == class_time2 and room1 == room2:
                json_data.append({
                    "classDay1": class_day1,
                    "classDay2": class_day2,
                    "classTime": class_time1,
                    "roomNumber": room1
                })

# Write the JSON data to the output file
with open(output_file, "w") as outfile:
    json.dump(json_data, outfile, indent=4)

print("Conversion completed! Check the output.json file.")
