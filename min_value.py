# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/18
# Generates 10 random numbers then uses a function
# And a FOR IN loop to calculate the minimum number.
# Displays it to user


# To generate a random number
import random


# Function to find the min value
def find_min_value(list_of_int):
    min_number = 100
    counter = 0
    # FOR IN loop to determine the min number
    for current_number in list_of_int:
        current_number = list_of_int[counter]
        if min_number > current_number:
            min_number = current_number
        counter = counter + 1
        if counter == 10:
            break
    return min_number


def main():
    # Variables
    list_of_integers = []
    MAX = 10
    MIN_VALUE = 0
    MAX_VALUE = 100
    counter = 0

    # FOR loop to add the numbers to the list
    for counter in range(MAX):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        list_of_integers.append(random_number)
        print("Added {} to the list".format(list_of_integers[counter]))
        counter = counter + 1

    # Calling the function and displaying the answer back to user
    min = find_min_value(list_of_integers)
    print("The smallest value is {}".format(min))


if __name__ == "__main__":
    main()
