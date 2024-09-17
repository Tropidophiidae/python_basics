import random
import string

# TASK 1

DICT_LIST_MIN = 2
DICT_LIST_MAX = 10
DICT_VALUE_MIN = 0
DICT_VALUE_MAX = 100
random_dicts = []


# function to generate random unique key letter
def get_random_letter(existing_dict):
    while True:
        random_letter = random.choice(string.ascii_lowercase)
        if random_letter not in existing_dict:
            return random_letter


# function to create dict of random letter-value pairs
def create_random_dict(number_of_keys):
    tmp_dict = {}
    for _ in range(number_of_keys):
        tmp_dict[get_random_letter(tmp_dict)] = random.randint(DICT_VALUE_MIN, DICT_VALUE_MAX)
    return tmp_dict


# get count of dicts
dict_count = random.randint(DICT_LIST_MIN, DICT_LIST_MAX)
print("Dict count:", dict_count)

# cycle to create fill list of random dicts
for _ in range(dict_count):
    dict_size = random.randint(DICT_LIST_MIN, DICT_LIST_MAX)
    random_dicts.append(create_random_dict(dict_size))

# print all dicts
for i in random_dicts:
    print(i)


# TASK 2
# check if dict contains already merged or original key
def get_merged_key(dict_to_find, starts_with_key):
    for key_from_dict_to_find in dict_to_find:
        if key_from_dict_to_find.startswith(starts_with_key):
            return key_from_dict_to_find
    return None


merged_dict = {}
# cycle to go throw all the dicts
for i in range(len(random_dicts)):
    # cycle to go throw all the keys
    for key, value in random_dicts[i].items():
        # get key
        merged_key = get_merged_key(merged_dict, key)
        # if key not present in merged_dict
        if merged_key is None:
            # add original key to merged_dict
            merged_dict[key] = value
        else:
            # else if key's value from random_dicts > merged key's value in merged_dict
            if value > merged_dict[merged_key]:
                # create name for new key
                new_key = key + '_' + str(i + 1)
                # remove old merged key value
                merged_dict.pop(merged_key)
                # add new key-value
                merged_dict[new_key] = value

print('=== result ===')
print(merged_dict)
