from src.main.model.astract_office_tool import AbstractOfficeTool
from src.main.model.brand import Brand
from src.main.model.colour import Colour


class Ruler(AbstractOfficeTool):
    def __init__(self, producer='def_producer', price_in_uah=0, brand=Brand(4),
                 colour=Colour(1), warranty_in_days=0, weight_in_grams=0, volume_in_liter=0):
        super().__init__(producer, price_in_uah, brand, colour, warranty_in_days, weight_in_grams)
        self.length_in_cm = volume_in_liter

    def __str__(self):
        return super().__str__()