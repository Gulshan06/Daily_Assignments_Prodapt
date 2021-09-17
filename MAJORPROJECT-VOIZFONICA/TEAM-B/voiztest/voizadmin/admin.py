from django.contrib import admin
from voizadmin.models import *


# Register your models here.
 
class profileCustomer(admin.ModelAdmin):
    fields = ("customer_name", "customer_DOB", "gender", "address", "pincode", "mobileno", "email", "adharno", "product_type", "customer_username","customer_password", "customer_photo", "customer_idfile", "customer_pic")
    

    search_fields = ("customer_name", "product_type", "mobileno",)
    
    list_display =[ 
        'customer_pic',
        'customer_name',
        'mobileno',
        'product_type',
        'created'
    ]
    list_display_links =[ 
        'customer_name',
        'mobileno' 

    ]

    list_filter = [ 
        'customer_name',
        'mobileno',
        'product_type',
        'created'
    ]
    # date_hierarchy = 'created'

    readonly_fields = ('created', 'customer_pic')


class profileEmployee(admin.ModelAdmin):
    fields =("empcode", "name", "address", "emailid", "phonenumber", "gender", "pincode", "aadhaarno", "empphoto", "empidfile", "dateofjoining","dateofbirth","salary","username","password", "employee_pic")

    list_display =[ 
        'employee_pic',
        'empcode',
        'name',
        'created'
    ]
    list_display_links =[ 
        'name',
        'empcode' 

    ]

    list_filter = [ 
        'empcode',
        'name',
        'created'
    ]

    readonly_fields = ('created', 'employee_pic')


class viewDongle(admin.ModelAdmin):
    fields =("dongle_modelname","dongle_modelpic", "dongle_InternetSpeed", "dongle_RouterSpeed", "dongle_description","dongle_price","dongle_quanity","dongle_pic")

    list_display =[ 
        'dongle_modelname',
        'dongle_pic',
        'dongle_price',
        'dongle_RouterSpeed'
    ]
    list_display_links =[ 
        'dongle_modelname',
        'dongle_RouterSpeed' 

    ]

    list_filter = [ 
        'dongle_modelname',
        'dongle_price',
        'created'
    ]

    readonly_fields = ('created','dongle_pic')


admin.site.register(Customer, profileCustomer)
admin.site.register(CustomerQuery)
admin.site.register(Employee, profileEmployee)
admin.site.register(DonglePurchase, viewDongle)
admin.site.register(CommonPage_Querry)

admin.site.register(PlanPrepaid)
admin.site.register(PlanPostpaid)
admin.site.register(recharge)
admin.site.register(DongleOrder)
admin.site.register(CustomerBillpay)
admin.site.register(CustomerUsage)


