from products.serializers import productSerializer
from products.models import product
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from products.models import product
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt 
def product_list(request):
    if(request.method == "GET"):
        pro = product.objects.all()
        pro_Serializer= productSerializer(pro, many=True)
        return JsonResponse(pro_Serializer.data, safe=False)

@csrf_exempt 
def product_update(request,fetchid):
    try:
        pro=product.objects.get(procode=fetchid)
        if (request.method == "GET"):
            pro_serialize = productSerializer(pro)
            return JsonResponse(pro_serialize.data,safe=False)
        
        
        if (request.method =='DELETE'):
            pro.delete()
            return HttpResponse("deleted",status=status.HTTP_404_NOT_FOUND)
        
        
        if(request.method == "PUT"):
            myproduct= JSONParser().parse(request)
            pro_serialize = productSerializer(data=myproduct)
            if(pro_serialize.is_valid()):
                pro_serialize.save()
                return JsonResponse(pro_serialize.data,status=status.HTTP_200_OK)
    
    except product.DoesNotExist:
        return HttpResponse ("Invalid bookid",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def details(request):
    if (request.method=="POST"):
        pdata= JSONParser().parse(request)
        product_serialize = productSerializer(data=pdata)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data) 
    else:
        return HttpResponse('no get method')