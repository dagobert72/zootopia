import json

# Load the JSON file
file_path = "animals_data.json"
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
    data = []

# Iterate through each animal in the data
if isinstance(data, list):  # Ensure the data is a list of animals
    for animal in data:
        if isinstance(animal, dict):  # Ensure each animal is represented as a dictionary
            # Print each field only if it exists
            if "Name" in animal:
                print(f"Name: {animal['Name']}")
            if "Diet" in animal:
                print(f"Diet: {animal['Diet']}")
            if "locations" in animal and isinstance(animal['locations'], list) and animal['locations']:
                print(f"First Location: {animal['locations'][0]}")
            if "Type" in animal:
                print(f"Type: {animal['Type']}")
            print()  # Add a blank line between animals for better readability
else:
    print("Error: Data is not in the expected format.")
