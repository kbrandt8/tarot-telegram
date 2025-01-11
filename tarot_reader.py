import os
import random

from dotenv import load_dotenv
from pymongo import MongoClient

from tarot_img import TarotImage

# ENVIRONMENT VARIABLES
load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')


class Reading:
    def __init__(self, num_of_cards):
        self.num_of_cards = num_of_cards
        self.cards = self.get_reading()

    def get_database(self):
        try:
            mongo = MongoClient(MONGO_URL)
            client = mongo['tarot-reader']
            return client
        except Exception as e:
            print(e)

    def get_reading(self):
        reader = self.get_database()
        reading = reader.cards.aggregate([{"$sample": {"size": self.num_of_cards}}])
        full_reading = self.format_reading(reading)
        self.get_image(full_reading)
        return full_reading

    def reversed(self):
        return True if random.randint(1, 10) > 4 else False

    def format_reading(self, reading):
        titles = ["Past", "Present", "Future"] \
            if self.num_of_cards == 3 \
            else ["Question", "Expectations", "Answer", "Why"]

        full_reading = [
            {'name': card['name'],
             'url': card['url'],
             'is_reversed': self.reversed(),
             'title': titles[index]}
            for (index, card) in
            enumerate(reading)]

        return full_reading

    def get_image(self, reading):
        tarot_image = TarotImage(reading)
        tarot_image.create_image()
