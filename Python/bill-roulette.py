import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_names = len(names)

random_int= random.randint(0,num_names - 1)
print(f"{names[random_int]} will pay the bill today!") 
