from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Supplier, Shop
from .serializer import SupplierSerializer


@api_view(['GET', 'POST'])
def supplier_list(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        # suppliers = sorted(suppliers)
        print(suppliers)
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def shop_search(request, query):
    shop = Shop.objects.filter(shop_name=query).values()
    if not shop:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(shop)


@api_view('POST')
def send_email(request, query):
    shop = Shop.objects.filter(shop_name=query).values()
    if not shop:
        return Response(status=status.HTTP_404_NOT_FOUND)
    send_mail(
        "Report of Shop: " + shop.shop_name,
        shop
    )
