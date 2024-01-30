# Program to create & display details of students:

students=[]

def insert():
        print("***************** Enter Student Details *****************")
        di = {}
        di['sid'] = int(input("Enter Student Id : "))
        di['name'] = input("Enter Student Name : ")
        di['age'] = int(input("Enter Student Age : "))
        students.append(di)
        print("Details Inserted....!!!")
        print()


def ShowAll():
        for dict in students:
                        print("************ Student Details ******************")
                        print("Student Id : ",dict['sid'])
                        print("Student Name : ",dict['name'])
                        print("Student Age : ",dict['age'])
                        print()
        


def select(studid):
        for dict in students:
                if (dict['sid'] == studid):
                        print("************ Student Details ******************")
                        print("Student Id : ",dict['sid'])
                        print("Student Name : ",dict['name'])
                        print("Student Age : ",dict['age'])
                        print()
def update(                       


while(True):
        print()
        print("***************************** Welcome *****************************")
        print("Press 1 For Insert Details.")
        print("Press 2 For Diplay All Details.")
        print("Press 3 For Diplay By Id.")
        print("Press 4 For Update.")
        print("Press 5 For Delete.")
        print("Press 6 For Exit.")
        ch = int(input())

        if(ch==1):
                insert()
        elif(ch==2):
                selectAll()
        elif(ch==3):
                sid = int(input("Enter Id for Select : "))
                selectById(sid)
        elif(ch==4):
                sid = int(input("Enter Id for Update Details: "))
                nname = input("Enter new name for update.")
                nage = int(input("Enter new Age for Update : "))
                update(sid,nname,nage)

        elif(ch==5):
                sid = int(input("Enter Id for Delete Details: "))
                delete(sid)

        elif(ch==6):
                print("********** Thank you********")
                break
        else:
                print("Invalid key Press...!!!")                                                   
    
