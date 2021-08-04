import sys,re,time,csv
try:
    header =['name','roll']]
    student= []
    class StudentData:
        def addDetails(self,name,ls,):
            totalmarks=sum(ls[2:])
            current_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
            dict1 = {'total':totalmarks,'name':name,'rollno':ls[0],'admin':ls[1],'english':ls[1],'hindi':ls[2],'maths':ls[3],'science':ls[4],'social':ls[5],'AddOn':current_time}
            student.append(dict1)
    obj1=StudentData()
    while(True):
        print("1. Add student details - ")
        print("2. Display student details Like API - ")
        print("3. Search student by Rollno - ")
        print("4. Ranking - ")
        print("5. Exit - ")
        choice = int(input('enter your choice - '))
        if choice==1:
            name = input("enter the name of student - ")
            rollno=input("enter the Rollno - ")
            # def val(rollno):
            #     val=re.search("^[1-9]",rollno)
            #     if val:
            #         return int(rollno)
            admin=input('enter the admin no -  ')
            english=input("enter the english marks: ")
            maths=input("enter the maths marks: ")
            social=input("enter the social marks: ")
            hindi=input("enter the hindi marks: ")
            science=input("enter the science marks: ")
            def val(rollno,admin,english,hindi,maths,science,social):
                val=re.search("^[1-9]",rollno)
                val1=re.search('^[1-9]',admin)
                val2=re.search('^[0-9]',english)
                val3=re.search('^[0-9]',maths)
                val4=re.search('^[0-9]',social)
                val5=re.search('^[0-9]',hindi)
                val6=re.search('^[0-9]',science)
                if val and val1 and val2 and val3 and val4 and val5 and val6:
                    return [int(rollno),int(admin),int(english),int(maths),int(social),int(hindi),int(science)]
                else:
                    print("you had enter wrong input")
                    sys.exit()
            # def addtimedate():
            #     time1=time.localtime()
            #     currenttime= time.strftime("%y-%m-%d  %H:%M:%S")
            #     return currenttime
            obj1.addDetails(name,val(rollno,admin,english,hindi,maths,science,social))
        if choice==2:
            print(student)
        if choice==3:
            srollno = int(input('enter the rollno to search - '))
            print(list(filter(lambda i:i['rollno']==srollno,student)))
        if choice == 4:
            print(sorted(student,reverse=True,key=lambda i:i['total']))
        if choice==5:
            sys. exit()
except Exception:
    print("You Enter something wrong")
else:
    print('your program is completed successfully')
finally:
    print("Thank you!!")


