# Program to validate a Password:

lower, upper, special, digit = 0,0,0,0
password = input(" Enter a password: ")

if(len(password)>=8 or len(password)==16):            
    for i in password:
         if(i == " "):
                print(" Not valid! Password should not contain spaces")
                continue
         if(i.isupper()):
                upper += 1        
         if(i.islower()):
                 lower += 1  
         if(i.isdigit()):
                digit += 1          
         if(i == '@' or i == '$' or i == '_' or i == '#'):
                special += 1
         
else:
    print("Password should be minimum of 8 characters")
    
if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1 and lower+upper+special+digit == len(password)):
    print("Valid Password")
else:
    print("Invalid Password")
