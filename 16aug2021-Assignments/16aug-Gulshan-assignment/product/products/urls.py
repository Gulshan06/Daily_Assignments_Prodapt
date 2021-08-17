from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add/',views.details,name='product_details'),
    path('all/',views.product_list,name='product_list'),
]
