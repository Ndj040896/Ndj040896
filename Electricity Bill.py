# Python Program to Calculate Electricity Bill:
 
units = int(input(" Enter Number of Units consumed : "))

if(units < 75):
    amount = units * 5.25
    
elif(units <= 125):
    amount = units * 7.50
    
elif(units <= 200):
    amount = units * 9.25
       
elif(units > 200):
    amount = units * 11.50
    
else:
    amount = units * 3.25
    surcharge = 10
    
total = amount 
print("\nElectricity Bill :",total)
