# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# # Change the value 20 in z to 30

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


def change_value(x):
    for i in range(len(x)):
        if 10 in x[i]:
            index = x[i].index(10)
            x[i][index] = 15
    return x


my_nested_list = [[5, 2, 3], [10, 8, 9]]
new_nested_list = change_value(my_nested_list)
print(new_nested_list)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][sports_directory['soccer'].index(
    'Messi')] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that,
# given a list of dictionaries, the function loops through each dictionary
# in the list and prints each key and the associated value. For example, given the following list:

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]



# def iterateDictionary(some_list):
#     # Loop through each dictionary in the list
#     for dictionary in some_list:
#         # Loop through each key-value pair in the dictionary
#         for key, value in dictionary.items():
#             # Print out the key and value for each pair
#             print(f"{key} - {value}", end=", ")
#         # Print a new line after each dictionary is printed
#         print()
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



# iterateDictionary(students)


# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored 
# in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2(key_name, some_list):
    # Loop through each dictionary in the list
    for dictionary in some_list:
        # Print the value for the given key in the current dictionary
        print(dictionary[key_name])

# Example usage with the given 'students' list
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along
# with the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    # Loop through each key in the dictionary
    for key in some_dict:
        # Print the name of the key and the size of its list
        print(f"{len(some_dict[key])} {key.upper()}")
        # Loop through each value in the list for the current key and print it
        for value in some_dict[key]:
            print(value)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
