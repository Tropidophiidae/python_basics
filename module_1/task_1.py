# constant for count of elements
import random

elements_count = 100
min_random = 0
max_random = 1000

# TASK: create list of 100 random numbers from 0 to 1000
# list to store random numbers
random_numbers = []

# cycle to make random list
for i in range(elements_count):
    # add random value to result list
    random_numbers.append(random.randint(min_random, max_random))

print("Generated list:", random_numbers)

# TASK: sort list from min to max(without using sort())
# bubble sort
for i in range(len(random_numbers) - 1):
    for j in range(len(random_numbers) - 1 - i):
        if random_numbers[j] > random_numbers[j + 1]:
            tmp = random_numbers[j]
            random_numbers[j] = random_numbers[j + 1]
            random_numbers[j + 1] = tmp

print("Sorted list:", random_numbers)

# TASK: calculate average for even and odd numbers
# list to store even numbers
even_numbers = []
# list to store odd numbers
odd_numbers = []

# Get even and odd numbers and store it in separate lists
# cycle for all numbers
for i in random_numbers:
    # if even -> add to even_numbers
    if i % 2 == 0:
        even_numbers.append(i)
    # if odd (not even) -> add to odd_numbers
    else:
        odd_numbers.append(i)

print("Even:", even_numbers)
print("Odd:", odd_numbers)


# Calculate Average for odd
# function for calculatin average
def get_average(numbers):
    # initial result as 0. Did it to use "+="
    res = 0
    # for each number in given list
    for n in numbers:
        # sum each number
        res += n
    # if res still = 0 (in case no numbers) return o, else calculate average
    return 0 if res == 0 else res / len(numbers)


average_even = get_average(even_numbers)
average_odd = get_average(odd_numbers)

print("Average even:", average_even)
print("Average odd:", average_odd)
