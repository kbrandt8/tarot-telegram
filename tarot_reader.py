import os
import random

from dotenv import load_dotenv
from pymongo import MongoClient

# ENVIRONMENT VARIABLES
load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')


class Reading():
    def __init__(self):
        pass

    def get_database(self):
        client = MongoClient(MONGO_URL)
        return client['tarot-reader']

    def get_reading(self, num_of_cards):
        reader = self.get_database()
        reading = reader.cards.aggregate([{"$sample": {"size": num_of_cards}}])
        full_reading = [{'name': card['name'], 'url': card['url'], 'is_reversed': self.reversed()} for card in reading]
        return full_reading

    def reversed(self):
        return True if random.randint(1, 10) > 4 else False

    # TYPES OF READINGS
    def three_card(self):
        reading = self.get_reading(3)
        titles = ["Past", "Present", "Future"]
        for card in reading:
            card['title'] = titles[reading.index(card)]
        return reading

    def four_card(self):
        reading = self.get_reading(4)
        titles = ["Question", "Expectations", "Answer", "Why"]
        for card in reading:
            card['title'] = titles[reading.index(card)]
        return reading
