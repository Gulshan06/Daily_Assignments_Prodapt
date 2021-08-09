import csv,smtplib,time,logging
import validation as v
try:
    header = ["productname","discription","price","manufacturer","manufacturingdate","expirydate","AddOn"]
    productlist=[]
    class ProductDetails:
        def addproductdetails(self,productname,discription,price,manufacturer,manufacturingdate,expirydate):
            current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
            dict1={"productname":productname,"discription":discription,"price":price,"manufacturer":manufacturer,"manufacturingdate":manufacturingdate,"expirydate":expirydate,'AddOn':current_time}
            productlist.append(dict1)
    obj1=ProductDetails()
    while(True):
        print("1.Add Products")
        print("2.View all products details")
        print("3.Customer service")
        print("4.List all the products that expired")
        print("5.Search the item by name")
        print("6.For CSV file")
        print("7.Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            productname=input("enter the product name - ")
            discription=input("enter the description of product - ")
            price=input("enter the price of product  - ")
            manufacturer=input("enter the manufacturer company name - ")
            manufacturingdate=input("enter product manufacturing date in mm-dd-yyyy format - ")
            expirydate=input("enter the expiry date in mm-dd-yyyy format - ")
            obj1.addproductdetails(productname,discription,v.val_price(price),manufacturer,manufacturingdate,expirydate)
        elif(choice==2):
            print(productlist)
        elif(choice==3):
            name= input("enter customer name -")
            emailid = input('enter customer emailid - ')
            total_product = []
            final_total=0
            for i in productlist:
                print('product name - ',i['productname'] ,' price of product - ',i['price'])
                a = int(input('if you want enter the number of Quntity (0 if you don\'t want)  -  '))
                total = i['price']*a
                final_total += total 
                if a > 0:
                    total_product.append(i["productname"])
                    total_product.append(i['price'])
                    total_product.append(a)
            print('customer name - ',v.val_name(name))
            print('customer emailid - ',v.val_emailid(emailid))
            print(total_product)
            print('your toatal amount is - ', final_total)
            discount = 0
            if (final_total<500):
                discount=final_total
            else:
                if (final_total > 500 and final_total <=1000):
                    f = (final_total/100)*10
                    discount = final_total - f
                elif (final_total >1000 and final_total <=2000):
                    f = (final_total/100)*20
                    discount = final_total - f
                elif (final_total >2000 and final_total <=3000):
                    f = (final_total/100)*30
                    discount = final_total - f
                elif (final_total >3000 and final_total <=4000):
                    f = (final_total/100)*40
                    discount = final_total - f
                elif (final_total >4000):
                    f = (final_total/100)*50
                    discount = final_total - f
            print('your total amount after discount is - ',discount)
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("gulshan062132@gmail.com","Gullu@2132")
            message='your total amount is - '+str(discount)
            connection.sendmail("gulshan062132@gmail.com",emailid, message)
            print("Message sended successful")
            connection.quit()
        elif(choice == 4):
            print("list all the products that expire  - ")
            current_date=time.strftime("%m-%d-%Y-",time.localtime())
            expired=(list(filter(lambda i:i["expirydate"]<str(current_date),productlist)))    
            if len(expired)>0:
                print(expired)
            else:
                print("No Expired product found")
        elif(choice == 5):
            S=input("enter the product that you want to search - ")
            print(list(filter(lambda i:i["productname"]==S,productlist)))
            
        elif(choice == 6):
            with open('Product.csv','w+',encoding='UTF8',newline='') as s:
                    writer = csv.DictWriter(s,fieldnames=header)
                    writer.writeheader()
                    writer.writerows(productlist)    
        elif(choice==7):
            break
except Exception:
    logging.error("Something went wrong")
else:
    print("Your program completed Successfully")
finally:
    print("Thank You!!")

