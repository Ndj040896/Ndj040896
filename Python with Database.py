import mysql.connector as con


connection = con.connect(host="localhost",port="3306",user="root",password="1234",database="navdeep")

if connection is not None:
    print("Connected..")
else:
    print("Error in Connection..!")

'''
class DBHelper:


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

obj = DBHelper()
'''
obj.insert_User(102,"Ajay Sharma","Indore","7896541230")
obj.insert_User(103,"Sumit Sharma","Hyderabad","7896541222")
obj.insert_User(104,"Jay Sharma","Bhopal","7896541233")
obj.insert_User(105,"Rahul Sharma","Indore","7896541235")


obj.update_User(102,"Raj Aryan","Mumbai","7896541111")
obj.delete_User(104)

obj.select_User()
'''
