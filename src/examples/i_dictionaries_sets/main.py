import dictionaries

phonebook = {}

key = input("Enter key: ")
value = input("Enter Value: ")

phonebook[key] = value

print(phonebook[key])

del phonebook[key]

print(phonebook)


















#phonebook = {'Chris': '555-1111', 'Katie': '555-222', 'Joanne': '555-3333'}
#print(phonebook)


#exists = dictionaries.is_key_in_dictionary('Chris', phonebook)

#print(exists)


#for key, value in phonebook.items():
    #print(key, value)





#print(phonebook['Chris'])
#print(phonebook['Katie'])

#for key in phonebook:
    #print(key, phonebook[key])

#print("values only")
#for value in phonebook.values():
    #print(value)
#print("dictionary items")
#for item in phonebook.items():
    #print(item)