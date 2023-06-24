strFileName = 'products.txt'
lstOfProductObjects = []

# --- Make the class ---
class Product():
# -- Constructor --
    def __init__(self, product_name: str, product_price: float):
# Attribute
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    # -- Product Name--

    @property  # You don't use for the getter's directive!
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Format attribute as Title case

    @product_name.setter  # The @NAME.setter must match the getter's name!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Product Price --
    @property  # You don't use for the getter's directive!
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price).title()  # Format attribute as Title case

    @product_price.setter  # The @NAME.setter must match the getter's name!
    def product_price(self, value):  # (setter or mutator)
        try:
            self.__product_price = float(value)
        except Exception as e:
            raise Exception("Price must be numbers \"n\t" + e.__str__().title())

#Methods
    def to_string(self):
        return self.product_name + ',' + str(self.product_price)
    def __str__(self):
        return self.to_string()

p1 = Product('proda', 9.99)
p2 = Product('prodB', 1.99)
lstOfProductObjects = [p1, p2]
for obj in lstOfProductObjects:
    print (obj.to_string())


