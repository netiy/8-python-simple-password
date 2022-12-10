password = open("pass.txt", "r").read()
while True:
    inputpassword = input("Enter password: ")
    if inputpassword == password:
        print("Access granted.")
        break
    else:
        print("Access denied.")
