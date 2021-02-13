class Restaurant():
    def __init__(self, name, c_type):
        self.restaurant_name = name
        self.cuisine_type = c_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Ресторан {self.restaurant_name.title()} имеет тип кухни - {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name.title()} открыт.")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, increment = 1):
        self.number_served += increment

class IceCreamStand(Restaurant):
    """Ресторан мороженого"""
    def __init__(self, name, c_type='мороженое'):
        super().__init__(name, c_type)
        self.flavors = ["ванильное", "пломбир", "лакомка"]

    def icecream_menu(self):
        print(f"Все виды мороженого: {self.flavors}")

restaurant = Restaurant("айвенго", "европейский")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)
restaurant.increment_number_served()
print(f"Количество клиентов: {restaurant.number_served}")

i_rest = IceCreamStand("ice")
i_rest.describe_restaurant()
i_rest.icecream_menu()

#rest2 = Restaurant("пересвет", "русский")
#rest3 = Restaurant("фудзияма", "японский")
#rest2.describe_restaurant()
#rest3.describe_restaurant()