# File paths
input_file = "text.txt"
output_file = "output.txt"

# Open the input file and the output file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Remove any trailing whitespace or newline characters
        line = line.strip()
        # Add the variable name and write to the output file
        outfile.write(f"classSchedule = {line}\n")

