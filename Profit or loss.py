# Program to claculate profit or loss:

Cost_Price = float(input(" Enter the cost price: "))
Selling_Price = float(input(" Enter the sell price: "))
 
if(Cost_Price - Selling_Price > 0):
    amount = Cost_Price - Selling_Price
    print("Total Loss Amount",amount)
elif(Selling_Price - Cost_Price > 0):
    amount = Selling_Price - Cost_Price
    print("Total Profit",amount)
else:
    print("No Profit & No Loss.")
