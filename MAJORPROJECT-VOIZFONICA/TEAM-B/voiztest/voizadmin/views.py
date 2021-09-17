from django.shortcuts import render, redirect
from voizadmin.models import *
from voizadmin.serializer import *
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.http import request
import requests
from django.http.response import HttpResponse,JsonResponse
from rest_framework import status
import json

from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from datetime import datetime,timedelta
import datetime

# Create your views here.


#......................Customer Management....................................#

# @csrf_exempt
# def collectcus(request):
#     if(request.method == 'POST'):
#         customer_serializer = CustomerSerializer(request.POST, request.FILES)

#         if(customer_serializer.is_valid()):
#             customer_serializer.save()
#             return HttpResponse("Customer Registration has done Successfully!")
#             #return JsonResponse(customer_serializer.data, status = status.HTTP_200_OK)
           
#             #return HttpResponse("Customer Registration has done Successfully!")

#         else:
#             return HttpResponse("Error in serialization", status = status.HTTP_400_BAD_REQUEST)

#     else:
#         return HttpResponse("Welcome !")


# To avoid repeating registration
@csrf_exempt
def customerValidation(request):
    if (request.method == "POST"):
        # customer_serializer = CustomerSerializer(request.POST, request.FILES)
        # if(customer_serializer.is_valid()):
            try:
                getName = request.POST.get("customer_name")
                getDOB = request.POST.get("customer_DOB")
                getGender = request.POST.get("gender")
                getAdd = request.POST.get("address")
                getPin = request.POST.get("pincode")
                getMob = request.POST.get("mobileno")
                getEmail = request.POST.get("email")
                getAdhar = request.POST.get("adharno")
                getProduct = request.POST.get("product_type")
                getUsername = request.POST.get("customer_username")
                getPassword = request.POST.get("customer_password")
                getPhoto = request.FILES["customer_photo"]
                getIdproof = request.FILES["customer_idfile"]

                customer_dic = {"customer_name":getName, "customer_DOB":getDOB, "gender":getGender, "address":getAdd, "pincode":getPin, "mobileno": getMob, "email":getEmail, "adharno":getAdhar, "product_type":getProduct, "customer_username":getUsername, "customer_password":getPassword, "customer_photo":getPhoto, "customer_idfile":getIdproof}
                print(customer_dic)
                cus = CustomerSerializer(data=customer_dic)
                print(cus)
                if cus.is_valid():
                    cus.save()
                    
                    return redirect(login)

                else:
                    print(cus.errors)



                # getcustomer= Customer.objects.filter(customer_name=getName, customer_DOB=getDOB, gender=getGender, address=getAdd, pincode=getPin, mobileno= getMob, email=getEmail, adharno=getAdhar, product_type=getProduct, customer_username= getUsername, customer_password=getPassword, customer_photo=getPhoto, customer_idfile=getIdproof)
                # cus_serialiser = CustomerSerializer(getcustomer, many=True, safe=False)
                

                # if (Customer.objects.filter(mobileno=getMob).exists()):
                #     return HttpResponse("Already Existing Mobile Number,  try with different Mobile Number! ")

                # elif (Customer.objects.filter(email=getEmail).exists()):
                #     return HttpResponse("Already Registered Email ID,  try with different Email ID ! ")

                # elif (Customer.objects.filter(adharno=getAdhar).exists()):
                #     return HttpResponse("Already Registered Aadhar No, give appropriate Aadhar ID proof number! ")
                
                # elif (Customer.objects.filter(customer_username=getUsername).exists()):
                #     return HttpResponse("Already Existing User name,  try with different user name! ")
                
                # else:
                #     cus_serialiser = CustomerSerializer(request.POST, request.FILES)
                #     if(cus_serialiser.is_valid()):
                #         cus_serialiser.save()
                #         return redirect(login)

                #     else:
                #         return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

                return HttpResponse("Successfull")

            except Customer.DoesNotExist:
                return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
            except:
                return HttpResponse("Something went wrong")





#Session
@csrf_exempt
def usercheck(request):
    try:
        getuser = request.POST.get("customer_username")
        getpassword = request.POST.get("customer_password")

        getCustomer = Customer.objects.filter(customer_username = getuser, customer_password = getpassword  )
        customer_serializer = CustomerSerializer(getCustomer, many=True)
        print(customer_serializer.data)

        if (customer_serializer.data):
            for n in customer_serializer.data:
                getId = n["id"]
                getName = n["customer_name"]
                getMobile = n["mobileno"]
                getEmail = n["email"]
                getProduct = n["product_type"]
                getAadhar = n["adharno"]
                getUsername = n["customer_username"]
                getPassword = n["customer_password"]
                getPhoto = n["customer_photo"]

            request.session['cid']=getId
            request.session['cname']=getName 
            request.session['cmob']=getMobile
            request.session['cemail']=getEmail
            request.session['cproduct']=getProduct
            request.session['caadhar']=getAadhar
            request.session['cuser']=getUsername
            request.session['cpassword']=getPassword
            request.session['cphoto']=getPhoto

            # cus_data = {"customer_name":getName, "mobileno":getMobile,"email":getEmail,"product_type":getProduct,"adharno":getAadhar,"customer_username":getUsername,"customer_password":getPassword, "customer_photo":getPhoto}
            #return render(request, "customerdashboard.html", {"data":cus_data})
            return redirect(cusDashboard)

        else:
            return HttpResponse("Invalid Credientials", status=status.HTTP_404_NOT_FOUND)

    except Customer.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong") 



def cusDashboard(request):
    try:
        getCid = request.session['cid']
        getcustomer = Customer.objects.get(id=getCid)
        cus_serialiser = CustomerSerializer(getcustomer)

        return render(request, "customerdashboard.html", {"data":cus_serialiser.data})

    except:
        return HttpResponse("Try again!")

def customerprofile(request):
    try:
        getCid = request.session['cid']
        getcustomer = Customer.objects.get(id=getCid)
        cus_serialiser = CustomerSerializer(getcustomer)

        return render(request, "customerprofile.html", {"data":cus_serialiser.data})

    except:
        return HttpResponse("Try again!")

#----------------------------------Dongle-------------------------------------------#

def dongle(request):
    try:
        getCid = request.session['cid']
        getcustomer = Customer.objects.get(id=getCid)
        cus_serialiser = CustomerSerializer(getcustomer, many=True)
        # return HttpResponse("successful!")
        return JsonResponse(cus_serialiser.data,safe=False,status=status.HTTP_200_OK)

    except:
        return HttpResponse("Try again!")


def pagedongle(request):
    don_serialiser= requests.get("http://127.0.0.1:8000/dongle/").json()
    return render(request, "buydongle.html", {"data_dongle":don_serialiser})


@csrf_exempt
def show_buyDongle(request):
    if(request.method == "GET"):
        buy = DonglePurchase.objects.all()
        buy_serialize = dongleitemsSerializer(buy,many =True)
        return JsonResponse(buy_serialize.data,safe=False,status=status.HTTP_200_OK)


def donglepage(request):
    # don= requests.get("http://127.0.0.1:8000/dongle/").json()
    buy = requests.get("http://127.0.0.1:8000/showallDongle/").json()

    return render(request, "buydongle.html", {"data_dongle":buy})
    # return render(request, "buydongle.html", {"data":don}, {"data_dongle":buy})


def dongleOrder(request):
    return render(request, 'dongleOrder.html') 


@csrf_exempt
def adddongleorder(request):
    if(request.method == 'POST'):
        order_serializer = dongleorderSerializer(data=request.POST)

        if(order_serializer.is_valid()):
            order_serializer.save()
            #return JsonResponse(order_serializer.data, status = status.HTTP_200_OK)
            return redirect(ordermail)
            
        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to Add Books Page!")


def ordermail(request):
    try:
        rec = request.session['cemail']
        current_date =datetime.datetime.now()
        # logintime = ' '.join(map(str, time))
        email = EmailMessage('Dongle Order Confirmation',' ''Your dongle order is confirmed and it will be deliver you shortly. Order booked time is' +str(current_date), to=[rec])
        email.send()
        # return HttpResponse('Mail send successfuly ')
        return redirect(confirmorder)

    except:
        return HttpResponse('something wrong ')

def confirmorder(request):
    return render(request, 'confirmOrder.html')



def logout(request):
   try:
      del request.session['cid']
   except:
      pass
#    return HttpResponse("<strong>You are logged out.</strong>")
   return redirect(log)

def log(request):
    try:
        rec = request.session['cemail']
        current_date =datetime.datetime.now()

        # logintime = ' '.join(map(str, time))
        email = EmailMessage('Loggedout from VoizFonica',' ''Your last logout session timing is ' +str(current_date), to=[rec])
        email.send()
        # return HttpResponse('Mail send successfuly ')
        return redirect(login)

    except:
        return HttpResponse('something wrong ')


def cushelp(request):
    try:
        getCid = request.session['cid']
        getcustomer = Customer.objects.get(id=getCid)
        cus_serialiser = CustomerSerializer(getcustomer)

        return render(request, "customerhelp.html", {"data":cus_serialiser.data})

    except:
        return HttpResponse("Try again!")

def Faqcus(request):
    try:
        getCid = request.session['cid']
        getcustomer = Customer.objects.get(id=getCid)
        cus_serialiser = CustomerSerializer(getcustomer)

        return render(request, "faqcus.html", {"data":cus_serialiser.data})

    except:
        return HttpResponse("Try again!")

 

#......................Customer Query....................................#

def contactus(request):
    return render(request, "contactus.html")


@csrf_exempt
def addcusquery(request):
    getType = request.POST.get("type")
    getMsg = request.POST.get("Message")

    getID = request.session['cid']
    getMobile = request.session['cmob']

    cus_query = {"customer_id":getID, "mobileno":getMobile, "type":getType, "Message":getMsg}
    query_serial = CusQuerySerializer(data=cus_query)
    if query_serial.is_valid():
        query_serial.save()
        return HttpResponse("Message Saved")

    else:
        return HttpResponse(query_serial.errors)


def showQuery(request):
    try:
        getID = request.session['cid']
        getMobile = request.session['cmob']

        getQuery = CustomerQuery.objects.filter(customer_id=getID, mobileno=getMobile )
        query_serializer = CusQuerySerializer(getQuery, many=True)

        return render(request, 'customerquery.html', {"data":query_serializer.data})

    except:
        return HttpResponse("Something went wrong, try again!")


#......................Billing Management....................................#

@csrf_exempt
def addbill(request):
    getCallduration = request.POST.get("mins_callduration")
    getCalltype = request.POST.get("call_type")
    getExistingRate = request.POST.get("ExistingPackRate")
    getRatemin = request.POST.get("extraCallRPM")
    getExtradata = request.POST.get("extraData")
    getMsgRate = request.POST.get("TotalMsgRate")
    getBill = request.POST.get("TotalBill")
    getBillissue = request.POST.get("Bill_issued")
    getBilldue = request.POST.get("Bill_due")
    

    getID = request.session['cid']
    getMobile = request.session['cmob']

    bill = { "customer_id":getID, "postpaid_customerMob":getMobile,"mins_callduration":getCallduration, "call_type":getCalltype,"ExistingPackRate":getExistingRate, "extraCallRPM":getRatemin,"extraData":getExtradata, "TotalMsgRate":getMsgRate,  "TotalBill":getBill, "Bill_issued":getBillissue, "Bill_due":getBilldue}
    bill_serial = BillSerializer(data=bill)
    if bill_serial.is_valid():
        bill_serial.save()
        return HttpResponse("Usage Saved")

    else:
        return HttpResponse(bill_serial.errors)

def showbill(request):
    try:
        getID = request.session['cid']
        getMobile = request.session['cmob']

        getShow = CustomerBillpay.objects.filter(customer_id=getID, postpaid_customerMob=getMobile )
        bill_serializer = BillSerializer(getShow, many=True)

        return render(request, 'billpay.html', {"data":bill_serializer.data})

    except:
        return HttpResponse("Something went wrong, try again!")


def billemail(request):
    rec = request.session['cemail']
    current_date =datetime.datetime.now()
    name = request.session['cname']
    phone = request.session['cmob']
        

        
        # logintime = ' '.join(map(str, time))
    email = EmailMessage('Dear'+str(name),' ''You have paid your Phone no '+str(phone),'' 'bill for August month Rs. 519. Paid timing is'+str(current_date), to=[rec])
    email.send()
        # return HttpResponse('Mail send successfuly ')
    return redirect(login)

    # except:
    #     return HttpResponse('something wrong ')





# Usage 
@csrf_exempt
def addusage(request):
    getDatausage = request.POST.get("Data_usage")
    getMsgusage = request.POST.get("Message_Usage")
    getRefill = request.POST.get("DataAndMsg_RefillTime")
    getCallbal = request.POST.get("CallBalance")
    getValidity = request.POST.get("Validity")
    

    getID = request.session['cid']
    getMobile = request.session['cmob']

    usage = { "customer_id":getID, "prepaid_customerMob":getMobile,"Data_usage":getDatausage, "Message_Usage":getMsgusage, "DataAndMsg_RefillTime":getRefill, "CallBalance":getCallbal, "Validity":getValidity}
    usage_serial = UsageSerializer(data=usage)
    if usage_serial.is_valid():
        usage_serial.save()
        return HttpResponse("Usage Saved")

    else:
        return HttpResponse(usage_serial.errors)

def showusage(request):
    try:
        getID = request.session['cid']
        getMobile = request.session['cmob']

        getShow = CustomerUsage.objects.filter(customer_id=getID, prepaid_customerMob=getMobile )
        usage_serializer = UsageSerializer(getShow, many=True)

        return render(request, 'BalUsage.html', {"data":usage_serializer.data})

    except:
        return HttpResponse("Something went wrong, try again!")





#-------Prepaid Recharge----------#

#prepaid plan
@csrf_exempt
def addpreplan(request):
    if(request.method == 'POST'):
        predata = JSONParser().parse(request)
        pre_serializer = PreSerializer(data= predata)

        if(pre_serializer.is_valid()):
            pre_serializer.save()
            return JsonResponse(pre_serializer.data, status = status.HTTP_200_OK)
            
        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to prepaid plan Page!")

@csrf_exempt
def showprepaid_api(request):
    if(request.method == "GET"):
        pre_plan = PlanPrepaid.objects.all()
        pre_serializer = PreSerializer(pre_plan, many=True)
        return JsonResponse(pre_serializer.data, safe=False, status = status.HTTP_200_OK)

    else:
        return HttpResponse("Welcome to view all !")

def showprepaidpage(request):
    pre=requests.get("http://127.0.0.1:8000/showprepaid/").json()
    return render(request, "prepaidpage.html", {"data":pre})

@csrf_exempt
def singlepreplan(request,fetchid):
    pre = PlanPrepaid.objects.get(plan_id= fetchid)
    if(request.method == 'GET'):
        preplan_serialize =  PreSerializer(pre)
        return JsonResponse(preplan_serialize.data, safe = False, status = status.HTTP_200_OK)




@csrf_exempt
def rechargehistory_api(request):
    if(request.method == "GET"):
        rec = recharge.objects.all()
        rec_serializer = RechargeSerializer(rec, many=True)
        return JsonResponse(rec_serializer.data, safe=False, status = status.HTTP_200_OK)

    else:
        return HttpResponse("Welcome to view all !")

    
def recHistory(request):
    rec = requests.get("http://127.0.0.1:8000/rechargehistory_api/").json()

    return render(request, "rechargehistory.html", {"data_dongle":rec})



#Postpaid

@csrf_exempt
def collectpostplan(request):
    if(request.method == 'POST'):
        post_serializer = PlanPostpaid(data = request.POST)

        if(post_serializer.is_valid()):
            post_serializer.save()
            return JsonResponse(post_serializer.data, status = status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome !")

@csrf_exempt
def view_postpaid_plan(request):
    if(request.method == "GET"):
        plan = PlanPostpaid.objects.all()
        plan_serialize = PostSerializer(plan,many =True)
        return JsonResponse(plan_serialize.data,safe=False,status=status.HTTP_200_OK)


def view_postpaid(request):
    plan = requests.get("http://127.0.0.1:8000/view_postpaid_plan/").json()
    return render(request,'postpaid.html',{'data':plan})





#......................Employee Management....................................#
@csrf_exempt
def collectemp(request):
    if(request.method == 'POST'):
        emp_serializer = EmployeeSerializer(request.POST, request.FILES)

        if(emp_serializer.is_valid()):
            emp_serializer.save()
            return HttpResponse("Registration has done Successfully!")
            #return JsonResponse(emp_serializer.data, status = status.HTTP_200_OK)
            #return redirect(addcustomerfile)


        else:
            return HttpResponse("Error in serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome !")



#......................Plan Views....................................#



#Buy Dongle

@csrf_exempt
def dongleImage(request):
    if(request.method == 'POST'):
        don_serializer = dongleitemsSerializer(request.POST, request.FILES)

        if(don_serializer.is_valid()):
            don_serializer.save()
            return HttpResponse("File uploaded Successfully!")

        else:
            return HttpResponse("Error in serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome !")



# def buydongle(request):
#     buy = requests.get("http://127.0.0.1:8000/showallDongle/").json()
#     return render(request,'buydongle.html',{'data':buy})




#......................Common Query....................................#

@csrf_exempt
def addcomQuery(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        query_serialize=comquerySerializer(data=request.POST)
        if(query_serialize.is_valid()):
            query_serialize.save()
            return HttpResponse("Your message uploaded successfully! We will reach you shortly.")
            #return JsonResponse(query_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)


# @csrf_exempt
# def viewQuery(request):
#     if(request.method=="GET"):
#         quries=CommonPage_Querry.objects.all()
#         query_serialize=comquerySerializer(quries,many=True)
#         return JsonResponse(query_serialize.data,safe=False)

#New HTML 

def common(request):
    return render(request, 'common.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def contacts(request):
    return render(request, 'contacts.html')

def Faq(request):
    return render(request, 'faq.html')

# def Dashboardhtml(request):
#     return render(request, 'customerdashboard.html')

#OLD
def addcustomer(request):
    return render(request, 'customerreg.html')

def addcustomerfile(request):
    return render(request, 'customerfile.html')

# def home(request):
#     return render(request, 'customerhead.html')


    




# def customerdashboard(request):
#     return render(request,'customerprofile.html')





#------------------New Connections and Sim----------------------------#

def new_presim(request):
    return render(request,"newprepaid.html")


@csrf_exempt
def new_simpre(request):
    if(request.method=="POST"):
        print(request.POST)
        # mydata=JSONParser().parse(request)
        customer_serial=CustomerSerializer(data=request.POST)
        if(customer_serial.is_valid()):
            customer_serial.save()
            # return redirect(viewall)
            return JsonResponse(customer_serial.data)
        else:
            return HttpResponse("error in serialization")

    else:
        return HttpResponse("sucess")



def new_postsim(request):
    return render(request,"newpostpaid.html")


@csrf_exempt
def new_simpost(request):
    if(request.method=="POST"):
        print(request.POST)
        # mydata=JSONParser().parse(request)
        customer_serial=CustomerSerializer(data=request.POST)
        if(customer_serial.is_valid()):
            customer_serial.save()
            # return redirect(viewall)
            return JsonResponse(customer_serial.data)
        else:
            return HttpResponse("error in serialization")

    else:
        return HttpResponse("sucess")


@csrf_exempt
def new_connection(request):
    if(request.method=="POST"):
        print(request.POST)
        connection_serial=ConnectionSerializer(data=request.POST)
        if(connection_serial.is_valid()):
            connection_serial.save()
            return HttpResponse("Your Connection is registered successful! We will reach you in 2 days")
        else:
            return HttpResponse("error in serialization")

    else:
        return HttpResponse("error occured")


def newConnection(request):
    return render(request,"newconnection.html")