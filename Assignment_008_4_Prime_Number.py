while True:
    user = int(input("Type done when you are finished! Please enter a number: ").strip())
    for i in range(2, user):
        if user == 1:
            check = True
        elif user % i == 0:
            check = False
            break
        else:
            check = True
    print(f"{user} is a prime number" if check else f"{user} is not a prime number")
