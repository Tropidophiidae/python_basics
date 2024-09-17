# constant for count of elements
import random

elements_count = 10
min_random = 0
max_random = 1000

# create list of 100 random numbers from 0 to 1000
# list to store random numbers
result = []

# cycle to make random list
for i in range(elements_count):
    # add random value to result list
    result.append(random.randint(min_random, max_random))

print("Generated list:", result)

# sort list from min to max (without using sort())
for i in range(len(result) - 1):

    for j in range(len(result) - 1 - i):
        #swap elements in they are in the wrong order
        if result[j] > result[j + 1]:
            tmp = result[j]
            result[j] = result[j + 1]
            result[j + 1] = tmp

print("Sorted list:", result)

