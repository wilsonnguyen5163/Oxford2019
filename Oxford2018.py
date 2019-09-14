

class Category:
    def __init__(self, types, brand, price, quantity, features):
        # types, name (brand), price/quantity, features
        self.types = types
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.features = features

    def cost_per_unit(self):
        return self.price/self.quantity

    def return_type(self):
        return self.types

    def return_features(self):
        return self.features

    def return_brand(self):
        return self.brand
