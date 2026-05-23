# Password Retry System

system_password = 231216
Guess = 0
running = True

while running:
  
  user_password = input("Enter password: ")
  
  if user_password.isdigit():
    user_password = int(user_password)
    Guess += 1

    if user_password == system_password:
     running = False
     print(f"congratulation you crack password in {Guess} chance")
    elif  Guess < 3  :
      print("Retry Again")

    else:
      print("Chance is over , try after 30 second !")
      running = False

  else:
    print("Enter only number understand")
  
    

