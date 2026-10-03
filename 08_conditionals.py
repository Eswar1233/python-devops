

user_input = int(input("Enter a number:"))

if user_input > 10:
  print("User input is greater than 10")
elif user_input <= 10 :
  print("Greta")
else:
  if user_input == 10:
    print("hello")
  else:
    print("Bye")



#  Exception Handling  --> try , except blocks
#  valueError, zero division error, i dentation error, type error, evnironment error



try:
  user_input = int(input("Enter a number try:"))
  if user_input > 10:
    print("User input is greater than 10")
  elif user_input <= 10 :
    print("Greta")
  else:
    if user_input == 10:
      print("hello")
    else:
      print("Bye")
except ValueError:
  print("please enter a number")