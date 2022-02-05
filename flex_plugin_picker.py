# a script that picks a random option from a file of options

# load the random module
import random

# open the file of options
options = open("options.txt", "r")

# read the file into a list
options_list = options.readlines()

# close the file
options.close()

# user inputs number
number = int(input("How many presets do you want? "))


# pick number of random options
for i in range(number):
    # pick a random option
    option = random.choice(options_list)
    # print the option
    print(option)