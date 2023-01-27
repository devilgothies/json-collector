import json
import csv

csvfile = open('cpuInfos.csv', 'w', newline='')
csvwriter = csv.writer(csvfile)

# Load the JSON file
with open("example.json") as json_file:
    data = json.load(json_file)

# Create an empty dictionary to store the host information
hosts_info = {}

# Iterate through the data in the JSON file
for host, host_data in data["hosts"].items():
    host_info = host_data["ansible_facts"]["system_info"]
    cpu_dump = host_info["cpu_info"]
    hostname_dump = host_info["hostname"]
    memory_dump = host_info["memory_info"]
    architecture = host_info["architecture"]

# Print JSON collected info
    print(hostname_dump)
    print(cpu_dump)
    print(memory_dump)
    print(architecture)

# Write a CSV file with collected info
    csvwriter.writerow([hostname_dump, cpu_dump, memory_dump, architecture])

