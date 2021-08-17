from seller.models import seller
from seller.serializers import sellerSerializer
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 
def seller_list(request):
    if(request.method == "GET"):
        sell = seller.objects.all()
        sell_Serializer= sellerSerializer(sell, many=True)
        return JsonResponse(sell_Serializer.data, safe=False)


@csrf_exempt
def seller_details(request):
    if (request.method=="POST"):
        getselName=request.POST.get("name")
        getselid=request.POST.get("id")
        getseladdress=request.POST.get("address")
        getselphoneno=request.POST.get("phoneno")
        sdata= {'sname':getselName ,'sid':getselid ,'saddress':getseladdress , 'sphoneno':getselphoneno} 
        seller_serialize = sellerSerializer(data=sdata)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data) 
    else:
        return HttpResponse('no get method')