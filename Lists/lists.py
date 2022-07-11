# lists in python

friends = ["Kavin", "Ben", "Mike", "Mike"] # store the values in a list inside []
print(friends) # return the list
print(friends[0]) # return the first value in the list
print(friends[-2]) # returns the value in the index starting from the last value
print(friends[1:3]) # returns a range of values
print(friends[1:]) # returns the second value and the rest after it


numbers = [4, 5, 9, 2, 10, 22, 16]

friends2 = friends.copy() # copy a list into a variable
friends.extend(numbers) # add all the elements in another array to an array
friends.append("Creed") # add a value to the array
friends.insert(1, "Kelly") # inserts a value in the index inputed
friends.remove("Ben") # removes a value from an array
friends.clear() # removes all the values from th array
friends.pop() # removes the last element from the list
numbers.sort() # returns the sorted list
numbers.reverse() # reverses the list
print(friends.index("Mike")) # returns the index of an element
print(friends.count("Mike")) # returns how many times an element occurs
print(friends)


