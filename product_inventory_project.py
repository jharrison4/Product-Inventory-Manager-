"""
application manages inventory of products.
keeps up with price, type of product, and quantity on hand.
can also sum up the total inventory value.

"""


class Product:

	def __init__(self, pid, price, quantity, name):
		self.pid = pid 
		self.price = price
		self.quantity = quantity
		self.name = name

	def __repr__(self):
		#Return the string representing the product
		return self.name


	def get_id(self):
		#returns id 
		return self.pid

	def get_price(self):
		#returns price
		return self.price

	def get_quantity(self):
		#returns quantity
		return self.quantity

	def increase_quantity(self):
		self.quantity += 1

	def decrease_quantity(self):
		self.quantity -= 1 


	def get_value(self):
		value = self.quantity * self.price
		return value


product_1 = Product('fishing', 20, 10, 'tackle box')
product_2 = Product('apparel', 30, 20, 'drake jacket')
#print("the product ID is located in {}".format(product_1.get_id()))
#print("the quantity is {}".format(product_1.get_quantity()))


#print(product_1)
#print(product_2)
#print(product_1.get_value())
#print(product_2.get_value())


class Inventory:

	def __init__(self, products):
		self.products = products
		self.fishing_list = []
		self.apparel_list = []
		self.value = 0

	def __repr__(self):
		return "Inventory(products: {}, fishing_list: {}, apparel_list: {}, value: {})".format(self.products, self.fishing_list, self.apparel_list, self.value)
	
	def add_fishing(self):
		for product in self.products:
			if product.get_id() == 'fishing':
				self.fishing_list.append(product)
		return '{} is in the fishing section'.format(self.fishing_list)

	def add_apparel(self):
		for product in self.products:
			if product.get_id() == 'apparel':
				self.apparel_list.append(product)
		return '{} is in the apparel section'.format(self.apparel_list)



	def add_total_value(self):
		total = []
		for product in self.products:
			total.append(product.get_value())
			for item in total:
				self.value += item 
		return self.value

			 


inventory_1 = Inventory([product_1, product_2])
inventory_1.add_fishing()
inventory_1.add_apparel()
inventory_1.add_total_value()

print(inventory_1)



















