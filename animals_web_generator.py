import json
import data_fetcher

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


def load_data(filename):
  with open(filename, 'r') as f:
    return json.load(f)


def generate_animal_html(animals):
  animal_html = ""
  for animal in animals:
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    lifespan = characteristics.get("lifespan", "Unknown")
    habitat = characteristics.get("habitat", "Unknown")
    locations = ", ".join(animal.get("locations", []))

    animal_html += f"""
        <div class="animal">
            <h2>{name}</h2>
            <p><strong>Diet:</strong> {diet}</p>
            <p><strong>Lifespan:</strong> {lifespan}</p>
            <p><strong>Habitat:</strong> {habitat}</p>
            <p><strong>Locations:</strong> {locations}</p>
        </div>
        """
  return animal_html


def create_html_page(animals_data, template_file="animals_template.html", output_file="animals.html"):
  try:
    with open(template_file, "r") as f:
      template = f.read()
  except FileNotFoundError:
    print(f"Error: Template file '{template_file}' not found.")
    return

  animals_html = generate_animal_html(animals_data)
  new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

  try:
    with open(output_file, "w") as f:
      f.write(new_html)
    print(f"HTML file '{output_file}' created successfully.")
  except Exception as e:
    print(f"Error writing to file: {e}")


# Example usage (assuming animals_data.json and animals_template.html exist):
try:
  animals_data = load_data('animals_data.json')
  create_html_page(animals_data)
except FileNotFoundError:
  print("Error: animals_data.json not found. Using sample data.")
  animals_data = [  # Sample Data if file not found
    {
      "name": "American Foxhound",
      "locations": ["North-America"],
      "characteristics": {
        "diet": "Omnivore",
        "lifespan": "10 to 12 years",
      }
    },
    {
      "name": "Arctic Fox",
      "locations": ["Eurasia", "Europe"],
      "characteristics": {
        "diet": "Carnivore",
        "lifespan": "7 - 10 years",
        "habitat": "Polar forest regions"
      }
    },
  ]
  create_html_page(animals_data)


  def main(data_fetcher):

    animal_name = input("Please enter an animal: ")
    data = data_fetcher.fetch_data(animal_name)

    if data:
      print(f"Data for '{animal_name}':")
      for idx, animal in enumerate(data, start=1):
        print(f"Animal {idx}:")
        print(f"  Name: {animal.get('name', 'Unknown')}")
        print(f"  Taxonomy: {animal.get('taxonomy', 'Unknown')}")
        print(f"  Locations: {animal.get('locations', 'Unknown')}")
        print(f"  Characteristics: {animal.get('characteristics', 'Unknown')}")
    else:
      print(f"No data found for the animal '{animal_name}' or an error occurred.")

if __name__ == "__main__":
  main()