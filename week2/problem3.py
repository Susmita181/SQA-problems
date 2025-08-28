def is_valid_password(s):
   
    if len(s) < 8:
        return False
    
 
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    

    for ch in s:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True
    

    return has_upper and has_lower and has_digit and has_special



password = input("Enter a string: ")

if is_valid_password(password):
    print("True")
else:
    print("False")
