import json
from pprint import pprint

def read(file_path):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def sort(dic):
    return dict(sorted(dic.items()))

def save(dic, file_path):
    # Save the sorted data to a new JSON file
    with open(file_path, 'w') as file:
        json.dump(dic, file, indent=4)

# Print the data
#pprint(sort(read('builds/Assassin.json')))