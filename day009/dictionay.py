# dictionary = {key01: value01, key02: value02, ..., key0N: value0N}

program_dictionary = {"BUG": "We find an error!", 
                    "NO_BUG": "No bug in the code",
                    "LOOP": "Repeat some piece of the code"}

print(program_dictionary["BUG"])

# adding new items to dictionary
program_dictionary["function"] = "piece of code ..."
print(program_dictionary)

empty_dic = {}

program_dictionary = {}
print(program_dictionary)

program_dictionary = {"BUG": "We find an error!", 
                    "NO_BUG": "No bug in the code",
                    "LOOP": "Repeat some piece of the code"}

# edit an item 
program_dictionary["BUG"] = "BUGS BUGS bugs ..."
print(program_dictionary)
print()

# loop through a dictionary
for key in program_dictionary:
    print(key)
    print(program_dictionary[key])
    print()