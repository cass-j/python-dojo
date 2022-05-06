#  Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 10
print(x)

students[0]['last_name']= 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y']= 30
print(z)
print("----------")



# Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for index in range(len(some_list)):
        print(f"first_name - {some_list[index]['first_name']}, last_name - {some_list[index]['last_name']}")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students)
print("")

#  Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for index in range(len(some_list)):
        print(f"{some_list[index][key_name]}")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
print("----------")


# Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    dict_keys = list(some_dict.keys())

    for index in range(len(dict_keys)):
        key_name = dict_keys[index]
        key_value = some_dict[key_name]
        print(f"{len(key_value)} {str.upper(key_name)}")
        # print(key_value)

        for value in range(len(key_value)):
            print(f"{key_value[value]}")
        
        print("----------")


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)