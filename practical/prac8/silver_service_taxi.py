"""
CP1404 Practical
SilverServiceTaxi class, derived from Taxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi has flagfall added to total bill and the price per km based on fanciness"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        return self.flagfall + super().get_fare()

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
