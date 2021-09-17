from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from voizadmin import views
from django.contrib import admin 

urlpatterns=[ 
    #New HTML
    
    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('contact/', views.contacts, name='contacts'),
    path('dongle/', views.dongle, name='dongle'),
    path('dongleOrder/', views.dongleOrder, name='dongleOrder'),
    path('cushelp/', views.cushelp, name='cushelp'),
    path('faqcommon/', views.Faq, name='Faq'),
    path('faq/', views.Faqcus, name='Faqcus'),
    #Billing System
    path('showbill/', views.showbill, name='showbill'),
    path('addbill/', views.addbill, name='addbill'),
    path('ebill/', views.billemail, name='billemail'),


    path('addusage/', views.addusage, name='addusage'),
    path('showusage/', views.showusage, name='showusage'),
    
    


    #New Apis
    path('usercheck/', views.usercheck, name='usercheck'),
    path('dashboard/', views.cusDashboard, name='cusDashboard'),
    path('myaccount/', views.customerprofile, name='myaccount'),
    path('donglepage/', views.donglepage, name='donglepage'),
    path('pagedongle/', views.pagedongle, name='pagedongle'),
    path('logout/', views.logout, name='logout'),
    path('log/', views.log, name='log'),


    path('addprepaid/', views.addpreplan, name='addpreplan'),
    path('showprepaid/', views.showprepaid_api, name='showprepaid_api'),
    path('singlepreplan/<fetchid>', views.singlepreplan, name='singlepreplan'),
    path('prepaidpage/', views.showprepaidpage, name='showprepaidpage'),


    path('collectpostplan/', views.collectpostplan, name='collectpostplan'),
    path('view_postpaid_plan/', views.view_postpaid_plan, name='view_postpaid_plan'),
    path('postpaidpage/', views.view_postpaid, name='view_postpaid'),

    #New connection
    path('connectionadd/', views.new_connection, name='new_connection'),
    path('connectionpage/', views.newConnection, name='NewConnection'),
   


    path('rechargehistory_api/', views.rechargehistory_api, name='rechargehistory_api'),
    path('recHistory/', views.recHistory, name='recHistory'),

    path('adddongleorder/', views.adddongleorder, name='adddongleorder'),
    path('ordermail/', views.ordermail, name='ordermail'),
    path('confirmorder/', views.confirmorder, name='confirmorder'),


    path('addcusquery/', views.addcusquery, name='addcusquery'),
    path('showallDongle/', views.show_buyDongle, name='show_buyDongle'),
    path('regcustomer/', views.customerValidation, name='customerValidation'),
    
    path('regemployee/', views.collectemp, name='collectemp'),
    
    path('dongleimg/', views.dongleImage, name='dongleImage'),


    
    path('addcomQuery/', views.addcomQuery, name='addcomQuery'),
    
    path('newprepaidsim/', views.new_simpre, name='new_simpre'),
    path('newpostpaidsim/', views.new_simpost, name='new_simpost'),

    
    
    #HTML
    path('addcustomer/', views.addcustomer, name='addcustomer'),
    path('fileupload/', views.addcustomerfile, name='addcustomerfile'),
    # path('home/', views.home, name='home'),
    
    # path('Dashboardhtml/', views.Dashboardhtml, name='Dashboardhtml'),
    
    

    path('newprepaid/', views.new_presim, name='new_presim'),
    path('newpostpaid/', views.new_postsim, name='new_postsim'),
   
   

    #Customer Query
    
    path('contactus/', views.contactus, name='contactus'),
    path('showQuery/', views.showQuery, name='showQuery'),


]


#Django Admin Panel customization
admin.site.site_header = "VoizFonica Admin"
admin.site.site_title = " Welcome to VoizFonica's Admin Page"
admin.site.index_title = " Welcome to VoizFonica Admin Portal"