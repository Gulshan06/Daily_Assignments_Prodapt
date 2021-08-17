from products.serializers import productSerializer
from products.models import product
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from products.models import product
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 
def product_list(request):
    if(request.method == "GET"):
        pro = product.objects.all()
        pro_Serializer= productSerializer(pro, many=True)
        return JsonResponse(pro_Serializer.data, safe=False)


@csrf_exempt
def details(request):
    if (request.method=="POST"):
        getproName=request.POST.get("pname")
        getprocode=request.POST.get("pcode")
        getprodescription=request.POST.get("pdescription")
        getproprice=request.POST.get("pprice")
        pdata= {'proname':getproName ,'procode':getprocode ,'prodescription':getprodescription , 'proprice':getproprice} 
        product_serialize = productSerializer(data=pdata)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data) 
    else:
        return HttpResponse('no get method')