def count_words(filename):
	try:
		with open(filename) as f_obj:
		    contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
	    #Count the approximate number of words in the file.
	    words = contents.split()
	    num_words = len(words)
	    print("The file " + repr(filename) + " has approximately " + str(num_words) + " words.")
	    
	    
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

