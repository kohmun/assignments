a, b = 1, 1
my_list = [a, b]
while b < 55:
    a, b = b, a + b
    my_list.append(b)
print(my_list)