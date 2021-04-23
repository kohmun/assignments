my_dict = {"Vedat" : "Vy2019.As", "Sedat" : "Sado@233.wo", "Clarusway":"NumberOne"}
user = input("Please enter your name: ").title()
if user in my_dict:
    print(f"Hello, {user}! The password is : {my_dict[user]}")
else:
    print(f"Hello, {user}! See you later.")