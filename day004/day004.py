# random module
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

# 0.0000... - 0.9999...
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Love score: {love_score}")

#print(my_module.pi)

# python list: data structure, python list is multable
# python_list = [item1, item2, ..., itemN], eache item can be of any type
                #     0     1     2     3     4                 
states_of_brazil = ["SP", "RJ", "RS", "SC", "BA"] # the order is important
print(states_of_brazil)
print(states_of_brazil[random.randint(0, len(states_of_brazil)-1)])
print(states_of_brazil[-1]) # start from the end
print(states_of_brazil[-2]) # start from the end

states_of_brazil[1] = "CE"
print(states_of_brazil)

states_of_brazil.append("MG")
print(states_of_brazil)

states_of_brazil.extend(["PA", "DF"])
print(states_of_brazil)

# list of lists
people_info = [["Ana", "Julia"], [25, 18]]
print(people_info)
