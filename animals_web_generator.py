import json

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

data = load_data('animals_data.json') # Load from file


def display_animal_info(animals):
  for animal in animals:
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})  # Handle missing characteristics
    diet = characteristics.get("diet", "Unknown")
    lifespan = characteristics.get("lifespan", "Unknown")
    habitat = characteristics.get("habitat", "Unknown")  # Use .get() here as well
    locations = ", ".join(animal.get("locations", []))

    print(f"Name: {name}")
    print(f"  Diet: {diet}")
    print(f"  Lifespan: {lifespan}")
    print(f"  Habitat: {habitat}")
    print(f"  Locations: {locations}")
    print("-" * 50)


display_animal_info(data)