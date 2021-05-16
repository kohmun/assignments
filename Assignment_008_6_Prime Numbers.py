my_list = [2, 3]
check = None
n = int(input("Please give me a whole positive number: ").strip())
for i in range(3,n,2):
    for v in range(3,i,2):
        if i%v==0:
            check = False
            break
        else:
            check = True
    if check:
        my_list.append(i)
print(my_list)
