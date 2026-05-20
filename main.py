import re

def check_password(password):
    score =0
    # lenth check 
    if len (password)>=8:
        score +=1
    else:
        print("Password shuld be atleast 8 charecters")

    if re.search(r"[A-Z]",password):
        score += 1
    else:
        print('Add an Uppercase Letter')

    if re.search(r"[0-9]",password):
        score +=1
    else:
        print("Add Number")
    
    if re.search(r"[!@#$%^&*]",password):
        score +=1
    else:
        print("Add a special charecter")

    if score ==4:
        print("Strong Password")
    elif score ==3:
        print("Medium password")
    else:
        print("Weak password")

password=input("Enter the Password: ")
check_password(password)
