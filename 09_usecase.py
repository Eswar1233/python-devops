# login system
username = "ec2-user"
password = "Devops321"

in_username = input("Please enter your username:")
in_password = input("Please enter your password:")

if (in_username == username) and (in_password == password):
    print("Login successfull")
else:
  print("Check your creds..wrong one")
  