# Program to enter name,age,id,city of 5 students in a liist & display them using a single object:

class Students:
       
    
    def Insert(self,name,age,Sid,city):
        self.name = name
        self.age = age
        self.Sid = Sid
        self.city = city
        obj = Students(name,age,Sid,city)
        ls.append(obj)

        
    def Display(self, obj):
          print("Name   : ", self.name)
          print("Age : ", self.age)
          print("Sid : ", self.Sid)
          print("City : ", self.city)
          print("\n")
          
ls = []
s1= Students()
print("\nList of students is:\n")
s1.Insert("hari",22,101,'sikkim')
s1.Insert("Ram",23,102,'ladakh')
s1.Insert("Lakshya",24,103,'manipal')
s1.Insert("Sriram",24,104,'rohtak')
s1.Insert("jai",23,105,'nepal')

print("Student Data is: ")
for i in range(ls.__len__()):
    s1.Display(ls[i])

                 
     
    
            
  
