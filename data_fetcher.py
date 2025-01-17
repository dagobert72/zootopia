import requests

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    }
    """
    API_URL = "https://example.com/api/animals"  # Replace with the actual API URL
    params = {"name": animal_name}  # Adjust parameters as required by the API

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()  # Assuming the API returns JSON data

        if not isinstance(data, list):
            raise ValueError("Unexpected data format: Expected a list of animals.")

        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return []
    except ValueError as e:
        print(f"Data parsing error: {e}")
        return []
