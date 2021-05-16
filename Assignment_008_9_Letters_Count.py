user = input("Please give me a sentence: ").strip()
my_dict = {}
my_list = list(sorted(user))
for i in my_list:
    if i in my_dict:
        continue
    else:
        my_dict[i] = my_list.count(i)
print(my_dict)
