# Program to claculate percentage of marks obtained in 5 subjects by a student:

S1 = float(input(" Enter subject 1 Marks: "))
S2 = float(input(" Enter subject 2 Marks: "))
S3 = float(input(" Enter subject 3 Marks: "))
S4 = float(input(" Enter subject 4 Marks: "))
S5 = float(input(" Enter subject 5 Marks: "))

total = S1 + S2 + S3 + S4 + S5
average = total / 5
percentage = (total / 500) * 100

print("Total Marks = %.2f"  %total)
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)     

if(percentage>=60):
                  print("Student passed in 1st Division.")
elif(percentage>=45):
                  print("Student passsed in 2nd Division.")
elif(percentage>=33):
                  print("Student passed in 3rd Division")
else:
      print("Fail.")

