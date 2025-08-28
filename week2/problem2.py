email = input("Enter an email: ")

if email.count("@") == 1 and email.count(".") == 1:
    at_index = email.index("@")
    dot_index = email.index(".")
    
    if (
        at_index > 0                     
        and dot_index > at_index + 1     
        and dot_index < len(email) - 2   
    ):
        print(True)
    else:
        print(False)
else:
    print(False)
