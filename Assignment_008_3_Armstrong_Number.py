while True:
    check = 0
    user = input("Type done when you are finished!. Please enter a number: ").strip()
    if user == "done":
        break
    elif not user.isdigit():
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
    for i in user:
        check += int(i)**len(user)
    if int(user) != check:
        print(f"{user} is not an Armstrong number")
    else:
        print(f"{user} is an Armstrong number")
