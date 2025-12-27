class ProductModel:
    def __init__(
        self,
        name,
        concentration,
        skin_types,
        ingredients,
        benefits,
        usage,
        side_effects,
        price
    ):
        self.name = name
        self.concentration = concentration
        self.skin_types = skin_types
        self.ingredients = ingredients
        self.benefits = benefits
        self.usage = usage
        self.side_effects = side_effects
        self.price = price
