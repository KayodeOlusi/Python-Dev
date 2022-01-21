# if-statement

is_hungry = True
is_old = False

if is_hungry:
    print("I'm humgry")
else:
    print("I'm ok")

if is_hungry or is_old:
    print("True")
else:
    print("False")

if is_hungry and is_old:
    print("True")
elif is_hungry or not(is_old):
    print("Ok")
else:
    print("False")

# ************************ Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num1 <= num2 and num1 <= num3:
        return num2
    else:
        return num3

print(max_num(1, 2, 3))