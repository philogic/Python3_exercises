import json
def greet_user():
	    filename = 'username.json'
    try:
        with open(filename) as f_obj:
	    username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dumo(username, f_obj)
		print("We'll remember you when you come back " + username + "!")
    else:
	print("Welcome back " + username + "!")
