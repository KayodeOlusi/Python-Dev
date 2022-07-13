# Reading from an external file

user_one = open("test1.txt", "r")
for line in user_one:
    print(line)
user_one.close()

# Editing an external file
user_two = open("test1.txt", "a")
user_two.write("\nEditing the file")
user_two.close()

# Overriding an external file
user_three = open("test1.txt", "w")
user_three.write("\nOverriding a file")
user_three.close()

# Creating a new file
user_four = open("test2.txt", "w")
user_four.write("\nCreating a new file")
user_four.close()