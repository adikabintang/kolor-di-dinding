'''
https://medium.com/@andreaspoyias/design-patterns-a-quick-guide-to-builder-pattern-a834d7cacead
'''

from abc import ABC, abstractmethod

# Product
class Pizza:
    def __init__(self):
        self.dough = ""
        self.topping = ""
        self.sauce = ""
    
    def set_dough(self, dough):
        self.dough = dough
    
    def set_topping(self, topping):
        self.topping = topping
    
    def set_sauce(self, sauce):
        self.sauce = sauce
    
    def __str__(self):
        return f"pizza with dough: {self.dough}, topping: {self.topping}, sauce: {self.sauce}"

# Abstract builder
class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = None
    
    def create_new_pizza_product(self):
        self.pizza = Pizza()
    
    def get_pizza(self):
        return self.pizza
    
    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_topping(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass
    
# concrete builder
class MargheritaConcreteBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.set_dough("marghertia dough")

    def build_topping(self):
        self.pizza.set_topping("margherita topping")

    def build_sauce(self):
        self.pizza.set_sauce("margherita sauce")

# concrete builder
class SpicyConcreteBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.set_dough("spicy dough")

    def build_topping(self):
        self.pizza.set_topping("spicy topping")

    def build_sauce(self):
        self.pizza.set_sauce("spicy sauce")

# Director
class CookDirector:
    def make_pizza(self, builder: PizzaBuilder):
        builder.create_new_pizza_product()
        builder.build_dough()
        builder.build_sauce()
        builder.build_topping()
        return builder.get_pizza()

if __name__ == "__main__":
    cook = CookDirector()
    margherita_builder = MargheritaConcreteBuilder()
    spicy_builder = SpicyConcreteBuilder()

    margherita_pizza = cook.make_pizza(margherita_builder)
    print(margherita_pizza)

    spicy_pizza = cook.make_pizza(spicy_builder)
    print(spicy_pizza)
