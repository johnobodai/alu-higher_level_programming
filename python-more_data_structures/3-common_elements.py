#!/usr/bin/python3
# Returns a set of common elements in both setsi


def common_elements(set_1, set_2):
    return set(set_1 & set_2)


'''
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
'''
