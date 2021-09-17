from django.db import models
from django.db.models.fields import CharField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars

import requests
# Create your models here.

class Customer(models.Model):
    customer_name=models.CharField(max_length=50, default='')
    customer_DOB=models.CharField(max_length=50,default='')
    gender=models.CharField(max_length=50, default='')
    address=models.CharField(max_length=50, default='')
    pincode=models.BigIntegerField(default='')
    mobileno=models.BigIntegerField(default='')
    email=models.EmailField(max_length=50, default='')
    adharno=models.BigIntegerField(default='')
    product_type=models.CharField(max_length=50, default='')
    customer_username=models.CharField(max_length=50, default='')
    customer_password=models.CharField(max_length=50, default='')
    customer_photo = models.ImageField(upload_to='images/', default=None)
    customer_idfile = models.ImageField(upload_to='files/', default=None)
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    # @property
    # def short_description(self):
    #     return truncatechars(self.mobileno, 15)

    def customer_pic(self):
        return mark_safe('<img src="{}" width ="100" />'.format(self.customer_photo.url))
    customer_pic.short_description ='Image'
    customer_pic.allow_tags = True


    # def __str__(self):
    #     return self.customer_name

    def __str__(self):
        return self.customer_name + "-" + self.email + "-" + self.product_type    
    
# class Customerfile(models.Model):
#     customer_photo = models.ImageField(upload_to='images/')
#     customer_idfile = models.FileField(upload_to='files/')
#     created = models.DateTimeField(auto_now_add=True)
#     id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

#--------------------------------------Customer Query-------------------------------------------#
class CustomerQuery(models.Model):
    customer_id = models.CharField(max_length=10, default= '')
    mobileno = models.CharField(max_length=15, default= '')
    type = models.CharField(max_length=15, default= '')
    Message = models.CharField(max_length=500, default = '')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def __str__(self):
        return self.type


#--------------------------------Plans------------------------------------------#

#--------For Prepaid-----------#


class PlanPrepaid(models.Model):
    plan_id = models.IntegerField(default='')
    preplan_name = models.CharField(max_length=50, default='')
    pre_description=models.CharField(max_length=500, default = '')
    pre_validity = models.CharField(max_length=100, default = '')
    preplan_type = models.CharField(max_length=100, default= '')
    pre_amount= models.IntegerField(default= '')
    data=models.DecimalField(max_digits=9, decimal_places=2, default='')
    msg = models.IntegerField(default='')
    voice = models.DecimalField(max_digits=9, decimal_places=2, default= '')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def __str__(self):
        return self.preplan_name + "-" + self.preplan_type 


class recharge(models.Model):
    fetchid = models.IntegerField(default='')
    mobileno=models.BigIntegerField(default='')
    product_type=models.CharField(max_length=50, default='')
    preplan_name = models.CharField(max_length=50, default='')
    pre_description=models.CharField(max_length=500, default = '')
    pre_validity = models.CharField(max_length=100, default = '')
    preplan_type = models.CharField(max_length=100, default= '')
    pre_amount= models.IntegerField(default= '')
    data=models.DecimalField(max_digits=9, decimal_places=2, default='')
    msg = models.IntegerField(default='')
    voice = models.DecimalField(max_digits=9, decimal_places=2, default= '')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)


    def save(self, *args, **kwargs):
        self.preplan_name= "199"
        self.pre_description="Unlimited, 1GB/Day, 100sms/day"
        self.pre_validity="28days"
        self.preplan_type="unlimited"
        self.pre_amount=199
        self.data=1000.00
        self.msg=100
        self.voice=10.00
        super().save(*args, **kwargs)

    def __str__(self):
        return self.mobileno+ "-" + self.preplan_name

    # def save(self, *args, **kwargs):
    #     plan = requests.get("http://127.0.0.1:8000/singlepreplan/<{self.fetchid}>")
    #     self.preplan_name=plan.json()
    #     self.pre_description=plan.json()
    #     self.pre_validity=plan.json()
    #     self.preplan_type=plan.json()
    #     self.pre_amount=plan.json()
    #     self.data=plan.json()
    #     self.msg=plan.json()
    #     self.voice=plan.json()
    #     super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     customer = requests.get("")
    #     self.mobileno= customer.json()
    #     self.product_type = customer.json()
    #     super().save(*args, **kwargs)

# class Postpaidplan(models.Model):
#     postplan_name=models.CharField(max_length=50, default = '')
#     postdescription=models.CharField(max_length=500, default = '')
#     monthly_rent= models.CharField(max_length=100,default = '')
#     postplan_type = models.CharField(max_length=100, default = '')
#     created = models.DateTimeField(auto_now_add=True)
#     id=models.AutoField(auto_created=True, primary_key=True, serialize=False)
 
#     def __str__(self):
#         return self.postplan_name + "-" + self.postplan_type + "-" + self.monthly_rent


class PlanPostpaid(models.Model):
    postplan_id = models.IntegerField(default='')
    postplan_name=models.CharField(max_length=50, default = '')
    postdescription=models.CharField(max_length=500, default = '')
    monthly_rent= models.CharField(max_length=100,default = '')
    postplan_type = models.CharField(max_length=100, default = '')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def __str__(self):
        return self.postplan_name + "-" + self.postplan_type + "-" + self.monthly_rent








    








#---------------------------Billing and BalanceUsage System Models-------------------------------#

class CustomerUsage(models.Model):
    customer_id = models.IntegerField(default = '')
    customerMob = models.CharField(max_length=100, default='')
    Data_usage = models.CharField(max_length=100, default='')
    Message_Usage = models.CharField(max_length=100, default='')
    DataAndMsg_RefillTime = models.CharField(max_length=100, default='')
    CallBalance = models.CharField(max_length=100, default='')
    Validity = models.DateField(default='')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def __str__(self):
        return self.customerMob



class CustomerBillpay(models.Model):
    customer_id = models.IntegerField(default = '')
    postpaid_customerMob = models.CharField(max_length=100, default='')
    mins_callduration = models.BigIntegerField(default='')
    call_type = models.CharField(max_length=100, default='')
    ExistingPackRate =models.BigIntegerField(default='')
    extraCallRPM = models.BigIntegerField(default='')
    extraData = models.CharField(max_length=100,default='')
    TotalMsgRate = models.CharField(max_length=100,default='')
    TotalBill = models.BigIntegerField(default='')
    Bill_issued = models.CharField(max_length=100, default='')
    Bill_due = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def __str__(self):
        return self.postpaid_customerMob



#---------------------------Employee Management---------------------------------------#

class Employee(models.Model):
    empcode=models.CharField(max_length=50, default='NO NAME',blank=True)
    name=models.CharField(max_length=50,default='NO NAME',blank=True)
    address=models.CharField(max_length=50,default='NO NAME',blank=True)
    emailid=models.EmailField(max_length=50,default='NO NAME',blank=True)
    phonenumber=models.CharField(max_length=50,default='NO NAME',blank=True)
    gender=models.CharField(max_length=50,default='NO NAME',blank=True)
    pincode=models.CharField(max_length=50,default='NO NAME',blank=True)
    aadhaarno=models.CharField(max_length=50,default='NO NAME',blank=True)
    empphoto = models.ImageField(upload_to='Empimages/',default='NO NAME',blank=True)
    empidfile = models.FileField(upload_to='Empfiles/',default='NO NAME',blank=True)
    dateofjoining=models.DateField(default='NO NAME',blank=True)
    dateofbirth=models.DateField(default='NO NAME')
    salary=models.CharField(max_length=50,default='NO NAME',blank=True)
    username=models.CharField(max_length=50,default='NO NAME',blank=True)
    password=models.CharField(max_length=50,default='NO NAME',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def employee_pic(self):
        return mark_safe('<img src="{}" width ="100" />'.format(self.empphoto.url))
    employee_pic.short_description ='Image'
    employee_pic.allow_tags = True

    def __str__(self):
        return self.empcode + "-" + self.name 


#----------------------------Dongle--------------------------------------------#
class DongleOrder(models.Model):
    name = models.CharField(max_length=50, default = '')
    mob_no = models.CharField(max_length=50, default = '')
    address = models.CharField(max_length=100, default = '')
    pincode = models.CharField(max_length=10, default = '')
    payment_method = models.CharField(max_length=50, default='Cash On Delivery')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)








class DonglePurchase(models.Model):
    dongle_modelname = models.CharField(max_length=50, default = '') 
    dongle_modelpic = models.ImageField(upload_to='DongleImg/', default = '') 
    dongle_InternetSpeed = models.CharField(max_length=50, default = '') 
    dongle_RouterSpeed = models.CharField(max_length=50, default = '') 
    dongle_description = models.CharField(max_length=100, default = '')   #No of device connection, Color 
    dongle_price = models.BigIntegerField(default = '')
    dongle_quanity = models.BigIntegerField(default = '')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def dongle_pic(self):
        return mark_safe('<img src="{}" width ="100" />'.format(self.dongle_modelpic.url))
    dongle_pic.short_description ='Image'
    dongle_pic.allow_tags = True

    def __str__(self):
        return self.dongle_modelname + "-" + self.dongle_RouterSpeed 



#--------------------------------Customer Query/Feedback System-------------------------------------#

#Customer Query Collection for non-customer of VoizFonica (In common page)
class CommonPage_Querry(models.Model):
    customername = models.CharField(max_length = 50, default = '')
    phone_no = models.BigIntegerField(default='')
    email_id = models.EmailField(max_length = 50, default = '')
    message = models.CharField(max_length=500,default='')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)


    def __str__(self):
        return self.customername + "-" + self.email_id


#.................................. Buy New Connection ........................................#

class NewConnection(models.Model):
    connection_type=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    mobile_no=models.BigIntegerField()
    email=models.EmailField(max_length=50, default='')
    address=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)











