# number = 0
# friends = ["Jim", "Karen", "Kevin"]

# for index in range(len(friends)):
#     print(friends[index])
    
# while number < 50:
#     print(number)
#     number += 2

def raise_to_power(base_num, pow_num):
    result = 1
    count = 1
    while count <= pow_num:
        result = result * base_num
        count += 1
    return result

print(raise_to_power(2, 3))