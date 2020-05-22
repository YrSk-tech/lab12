from src.main.model.brand import Brand
from src.main.model.colour import Colour


class AbstractOfficeTool:

    def __init__(self, producer='def_producer', price_in_uah=0, brand=Brand(4), colour=Colour(8), warranty_in_days=0,
                 weight_in_grams=0):
        self.producer = producer
        self.price_in_uah = price_in_uah
        self.brand = brand
        self.colour = colour
        self.warranty_in_days = warranty_in_days
        self.weight_in_grams = weight_in_grams

    def str(self):
        return "Producer {}, Price in uah {}, Brand {}, Colour {}, Warranty in days {}, Weight in grams {}".format(
            self.producer, self.price_in_uah, self.brand, self.colour, self.warranty_in_days, self.weight_in_grams)