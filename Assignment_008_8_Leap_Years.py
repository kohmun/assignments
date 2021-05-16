while True:
    user = input("Type done when you are finished! Please give me a year: ").strip()
    if user == "done":
        break
    else:
        user = int(user)
    check = bool(user%4==0 and not user%100==0 or user%400==0)
    if check:
        print(f"{user} is a leap year")
    else:
        print(f"{user} is not a leap year")