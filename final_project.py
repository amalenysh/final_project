from typing import List
from Processing import bake, delivery


class Pizza:
    def __init__(self, name: str, composition: List[str], size: str = 'L'):
        """
        Class for all types of pizzas
        name: name of pizza
        composition: ingredients for pizza
        size: size of the pizza (default is L)
        """
        self.sizes = ['L', 'XL']
        if size not in self.sizes:
            raise ValueError('This size is not available')
        self.name = name
        self.composition = composition
        self.size = size

    def dict(self):
        """
        Makes a dict out of recipe
        """
        return {self.name: self.composition}


class Margherita(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Class for pizza Margherita
        """
        super().__init__('Margherita', ['tomato sauce', 'mozzarella', 'tomatoes'], size)

    def __str__(self):
        return 'Margherita 🧀'


class Pepperoni(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Class for pizza Pepperoni
        """
        super().__init__('Pepperoni', ['tomato sauce', 'mozzarella', 'pepperoni'], size=size)

    def __str__(self):
        return 'Pepperoni 🍕'


class Hawaiian(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Class for Hawaiian pizza
        """
        super().__init__('Hawaiian', ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'], size=size)

    def __str__(self):
        return 'Hawaiian 🍍'


class Order:
    def __init__(self,  pizza: Pizza):
        """
        Class for order details (of it was baked and delivered)
        """
        self.pizza = pizza

        self.baked = 0
        self.delivered = 0

    def bake(self):
        """
        Bakes a pizza
        """
        self.baked = 1
        return bake(self.pizza)

    def deliver(self):
        """
        Delivers pizza
        """
        self.delivered = 1
        return delivery(self.pizza)
