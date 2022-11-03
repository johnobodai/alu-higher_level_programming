#!/usr/bin/python3i
# Returns a key with the biggest integer value


def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    initial_max_key = list(a_dictionary.keys())[0]
    initial_max_value = a_dictionary[initial_max_key]
    for i, j in a_dictionary.items():
        if j > initial_max_value:
            initial_max_value = v
            initial_max_key = i
    return (initial_max_key)

