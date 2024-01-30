# Program to validate Email id:


email = input("Enter an email: ")
d=0
s=0

for i in email:
    if(i.isspace()):
          s +=1

if(email.endswith('.com')):
         d = email.index('.com') - email.index('@')
elif(email.endswith('.in')):
         d = email.index('.in') - email.index('@')    


if(email.count('@')== 1 and d>3 and email[0].isalpha() and s==0):
   print(" Valid Email")
else:
   print("Invalid Email")
          
          
