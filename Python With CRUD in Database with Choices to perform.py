import mysql.connector as con
'''
import pypyodbc
from insert import Insert
from update import Update
from delete import Delete
from select import Select
'''

class DBHelper:
    '''
        def main():
          print('Available Options: 1=insert_User, 2=update_User, 3=delete_User, 4=select_User')
          choice = input('Choose your option = ')

        if choice == '1':
           i=insert_User()
           i.insert_User()
        elif choice == '2':
           u = update_User()
           u.func_UpdateData()
        elif choice == '3':
           d = delete+User()
           d.delete_User()
        elif choice == '4':
           s = select_User ()
           s.select_User()    
        else:
           print('Wrong choice.')
          main() 
     '''

 
        def __init__(self):
                self.conn = con.connect(host="localhost",port="3306",user="root",password="1234",database="navdeep")
                query = "create table if not exists user(uid int primary key,name varchar(45),city varchar(45),mobile varchar(15))"
                self.cur   =  self.conn.cursor()
                self.cur.execute(query)
                print("Table Created Successfully...!!!")


        def insert_User(self,uid,name,city,mobile):
                query = "insert into user(uid,name,city,mobile) values ({},'{}','{}','{}')".format(uid,name,city,mobile)
                self.cur.execute(query)
                self.conn.commit()
                print("Data Inserted Successfully...!!!")




        def update_User(self,uid,nname,ncity,nmobile):
                query = "update user set name='{}',city='{}',mobile='{}' where uid={}".format(nname,ncity,nmobile,uid)
                self.cur.execute(query)
                self.conn.commit()
                print("Data Updated Successfully...!!!")
                

        def delete_User(self,uid):
                query ="delete from user where uid={}".format(uid)
                self.cur.execute(query)
                self.conn.commit()
                print("User Deleted Successfully...!!!")

        def select_User(self):
                query = "select * from user"
                self.cur.execute(query)
                for i in self.cur:
                        print("************ User Details ***************")
                        print("User id is : ",i[0])
                        print("User Name is : ",i[1])
                        print("User Name is : ",i[2])
                        print("User Name is : ",i[3])
                        print()
                        


'''                        
while(True):
        print()
        print("***************** Welcome *******************")
        print("Press 1 For Insert Details.")
        print("Press 2 For Update all Details.")
        print("Press 3 For Delete.")
        print("Press 4 For Select.")
        print("Press 5 For Exit.")
        ch = int(input())

        if(ch==1):
                insert_User()
                
        elif(ch==2):
                sid = int(input("Enter new Id to Update Details: "))
                nname = input("Enter new name to update.")
                ncity = input("Enter new city to Update : ")
                nmobile = int(input("Enter new mobile number to Update : "))
                update_User(sid,nname,nage)
                
        elif(ch==3):
                sid = int(input("Enter Id for Delete Details: "))
                delete_User(sid)
                
        elif(ch==4):
                sid = int(input("Enter Id for Select : "))
                select_User(sid)
                
        elif(ch==5):
                print("********** Thank you********")
                break
        else:
              print("Invalid key Press...!!!")


obj = DBHelper()

obj.insert_User(102,"Ajay Sharma","Indore","7896541230")
obj.insert_User(103,"Sumit Sharma","Hyderabad","7896541222")
obj.insert_User(104,"Jay Sharma","Bhopal","7896541233")
obj.insert_User(105,"Rahul Sharma","Indore","7896541235")

obj.update_User(102,"Raj Aryan","Mumbai","7896541111")
obj.delete_User(104)

obj.select_User()
'''
