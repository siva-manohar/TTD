correct_passowrd = "Siva@12345"
presented_passowrd = ""

while presented_passowrd != correct_passowrd:
    presented_passowrd = input("enter your passowrd: ")
    if presented_passowrd != correct_passowrd:
        print("Invalid password.. Try again")
print("login successfull")