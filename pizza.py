def make_pizza(size, *toppings):
	"""Summarize the pizza we are abvout to make"""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
