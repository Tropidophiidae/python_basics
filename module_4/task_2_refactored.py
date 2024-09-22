import random
import string

# TASK 1

DICT_LIST_MIN = 2
DICT_LIST_MAX = 10
DICT_VALUE_MIN = 0
DICT_VALUE_MAX = 100


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


def create_list_of_random_dicts(_dict_count):
    tmp = []
    for _ in range(_dict_count):
        dict_size = random.randint(DICT_LIST_MIN, DICT_LIST_MAX)
        tmp.append(create_random_dict(dict_size))
    return tmp


# get count of dicts
dict_count = random.randint(DICT_LIST_MIN, DICT_LIST_MAX)
print("Dictionaries count:", dict_count)

# cycle to create fill list of random dicts
random_dicts = create_list_of_random_dicts(dict_count)

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


def merge_key(_dict, _new_key, _old_key, _value):
    # create name for new key
    # remove old merged key value
    _dict.pop(_old_key)
    # add new key-value
    _dict[_new_key] = _value


def merge_one_dict(_dicts_to_merge, _dict_number, _merged_dict):
    # cycle to go throw all the keys
    for k, v in _dicts_to_merge[_dict_number].items():
        # get key
        _merged_key = get_merged_key(_merged_dict, k)
        # if key not present in merged_dict
        if _merged_key is None:
            # add original key to merged_dict
            _merged_dict[k] = v
        else:
            # else if key's value from random_dicts > merged key's value in merged_dict
            if v > _merged_dict[_merged_key]:
                merge_key(_merged_dict, k + '_' + str(_dict_number + 1), _merged_key, v)


merged_dict = {}
# cycle to go throw all the dicts
for i in range(len(random_dicts)):
    merge_one_dict(random_dicts, i, merged_dict)

print('=== result ===')
print(merged_dict)
