responses = {}

polling_active = True

while polling_active == True:
	name = input("What is your name? ")
	response = input("\nWhich mountain would you like to cliomb someday? ")
	responses[name] = response
	
	repeat = input("Would you like to let another person respond (yes/no) ")
	if repeat == 'no':
		polling_active = False
		
print("\n---Poll results---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")
