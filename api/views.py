from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductSerializer

# Create your views here.
class AddProduct(APIView):
    def post(self, request):
        try:
            data_dict = {
                "name": request.data["name"],
                "description": request.data["description"],
                "price": float(request.data["price"]),
                "category": request.data["category"],
                "image": request.data["image"],
            }
            data_serializer = ProductSerializer(data=data_dict)
            if data_serializer.is_valid():
                data_serializer.save()
                return Response({"message": "Product added successfully"}, status=status.HTTP_200_OK)
            else:
                print(data_serializer.errors)
                return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)