from rest_framework import serializers
from django.db.models import fields
from voizadmin.models import *

class CustomerSerializer(serializers.ModelSerializer):
    customer_photo =serializers.ImageField()
    customer_idfile=serializers.ImageField()
    class Meta:
        model = Customer
        fields = ("customer_name", "customer_DOB", "gender", "address", "pincode", "mobileno", "email", "adharno", "product_type", "customer_username","customer_password", "customer_photo", "customer_idfile","created", "id")


class CusQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =("id", "created", "customer_id", "mobileno", "type", "Message")


class PreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanPrepaid
        fields = ("plan_id","preplan_name", "pre_description", "pre_validity", "preplan_type", "pre_amount", "data", "msg", "voice", "created", "id" )

class RechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = recharge
        fields = ("mobileno", "product_type","preplan_name", "pre_description", "pre_validity", "preplan_type", "pre_amount", "data", "msg", "voice", "created", "id" )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanPostpaid
        fields = ("postplan_id","postplan_name","postdescription", "monthly_rent", "postplan_type", "created", "id" )


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUsage
        fields = ("customer_id", "customerMob", "Data_usage", "Message_Usage", "DataAndMsg_RefillTime", "CallBalance", "Validity", "created", "id")

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBillpay
        fields = ("customer_id", "postpaid_customerMob", "mins_callduration", "call_type", "ExistingPackRate", "extraCallRPM", "extraData", "TotalMsgRate", "TotalBill", "Bill_issued", "Bill_due", "created", "id")

class EmployeeSerializer(serializers.ModelSerializer):
    empphoto=serializers.ImageField()
    empidfile=serializers.ImageField()
    class Meta:
        model = Employee
        fields = ("empcode", "name", "address", "emailid", "phonenumber", "gender", "pincode", "aadhaarno", "empphoto", "empidfile", "dateofjoining","dateofbirth","salary","username","password", "created", "id")



class dongleitemsSerializer(serializers.ModelSerializer):
    dongle_modelpic=serializers.ImageField()
    class Meta:
        model = DonglePurchase
        fields = ("dongle_modelname","dongle_modelpic", "dongle_InternetSpeed", "dongle_RouterSpeed", "dongle_description","dongle_price", "dongle_quanity", "created","id")


class dongleorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DongleOrder
        fields = ("name","mob_no","address", "pincode", "payment_method", "created", "id")
        


class comquerySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonPage_Querry
        fields = ("customername", "phone_no", "email_id", "select_type", "message", "created", "id")


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewConnection
        fields =('id','connection_type','name','mobile_no','email','address','date')