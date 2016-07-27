def describe_pet(pet_name, animal_type = 'dog'):
	"""Display information about the pet."""
	print("\nI have a " + animal_type + ".")
	print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')
describe_pet('willie', 'cat')
describe_pet()
