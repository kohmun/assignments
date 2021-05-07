if input("Are you a cigarret addict older than 75 years old?").title() == "Yes": 
  age = True 
else: 
  age = False
if input("Do you have a severe chronic desease?").title() == "Yes": 
  chronic = True 
else: 
  chronic = False
if input("Is your immune system too weak?").title() == "Yes": 
  immune = True 
else: 
  immune = False
if age or chronic or immune:
  print("You are in risky group")
else: 
  print("You are not in risky group")