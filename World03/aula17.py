num = [2, 5, 9, 1, 9, 3, 6, 2, 7, 0, 4]
print(num)
num[2] = 3
print(num)

# Add value
# APPEND insert a new item in the end.
num.append(7)
print('Append\n', num)
# INSERT can uses an index to determine where to add the value.
num.insert(2, 0)
print('Insert\n', num)

# SORT
num.sort()
print('Sort\n', num)
# Sort in reverse mode 2 ways
num.reverse()
print('reverse\n', num)
num.sort(reverse=True)
print('sort(reverse=True)\n', num)
print(f'len \n', len(num))

# Removing
# POP uses an index as parameter
num.pop()
print('pop()\n', num)
num.pop(2)
print('pop(2)\n', num)
# REMOVE uses the content as parameter
# to remove you may first check if the value exists
if 8 in num:
    num.remove(8)
    print('remove(8)\n', num)
else:
    print('Valor não está na lista.')
num.remove(2)
print('remove(2)\n', num)
# DEL works like pop
del num[6]
print('del num[6]\n', num)
