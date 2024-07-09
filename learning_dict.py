info = {'name':'Ronak', 'age':23, 'eligible':True}

#This print statement will give an error if the key is not present in the dictionary
print(info['name']) 

#This print statement wont give an error if the key is not present in the dictionary
print(info.get('name'))

#This print statement will print all the values in the dictionary
print(info.values())

#This print statement will print all the keys in the dictionary
print(info.keys())

#This print statement will print all the items in the dictionary
print(info.items())