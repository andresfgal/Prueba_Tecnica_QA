
import unittest
import requests
from random import randint

# URLs base
BASE_URL_PEOPLE = "https://www.swapi.tech/api/people/"
BASE_URL_PLANETS = "https://www.swapi.tech/api/planets/"
BASE_URL_STARSHIPS = "https://www.swapi.tech/api/starships/"


PEOPLE_ID_RANGE = (1, 83)  
PLANETS_ID_RANGE = (1, 60)  
STARSHIPS_ID_RANGE = (2, 36)   

class SwapiAPITest(unittest.TestCase):
    def test_get_random_person(self):
        random_id = randint(*PEOPLE_ID_RANGE)
        response = requests.get(BASE_URL_PEOPLE + str(random_id))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("result", data)
        self.assertIn("name", data["result"]["properties"])

    def test_get_random_planet(self):
        random_id = randint(*PLANETS_ID_RANGE)
        response = requests.get(BASE_URL_PLANETS + str(random_id))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("result", data)
        self.assertIn("name", data["result"]["properties"])

    def test_get_random_starship(self):
        random_id = randint(*STARSHIPS_ID_RANGE)
        response = requests.get(BASE_URL_STARSHIPS + str(random_id))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("result", data)
        self.assertIn("name", data["result"]["properties"])

    def test_invalid_person_id(self):
        response = requests.get(BASE_URL_PEOPLE + "99999")
        self.assertEqual(response.status_code, 404)

    def test_invalid_planet_id(self):
        response = requests.get(BASE_URL_PLANETS + "99999")
        self.assertEqual(response.status_code, 404)

    def test_invalid_starship_id(self):
        response = requests.get(BASE_URL_STARSHIPS + "99999")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
