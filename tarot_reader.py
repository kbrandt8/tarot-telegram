import os
import random

from pymongo import MongoClient

from dotenv import load_dotenv
load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')


class Reading():
    def __init__(self):
        pass

    def get_database(self):
        client = MongoClient(MONGO_URL)
        return client['tarot-reader']

    def reversed(self):
        return True if random.randint(1, 10) > 4 else False

    def get_reading(self, num_of_cards):
        reader = self.get_database()
        reading = reader.cards.aggregate([{"$sample": {"size": num_of_cards}}])
        full_reading = [{'name': card['name'], 'url': card['url'], 'is_reversed': self.reversed()} for card in reading]
        return full_reading
    def three_card(self):
        reader = self.get_database()
        reading = reader.cards.aggregate([{"$sample": {"size": 3}}])
        titles=["Past","Present","Future"]
        full_reading = [{'name': card['name'], 'url': card['url'], 'is_reversed': self.reversed()} for card in reading]
        for card in full_reading:
            card['title'] = titles[full_reading.index(card)]
        return full_reading

    def four_card(self):
        reader = self.get_database()
        reading = reader.cards.aggregate([{"$sample": {"size": 4}}])
        titles=["Question","Expectations","Answer","Why"]
        full_reading = [{'name': card['name'], 'url': card['url'], 'is_reversed': self.reversed()} for card in reading]
        for card in full_reading:
            card['title'] = titles[full_reading.index(card)]
        return full_reading