from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, User, Follow, Purchase
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer, UserSerializer, FollowSerializer, PurchaseSerializer

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

class AddUser(APIView):
    def post(self, request):
        try:
            data_dict = {
                "email": request.data["email"],
                "balance": float(request.data["balance"]),
            }
            if User.objects.filter(email=data_dict["email"]).exists():
                return Response({"message": "User already exists"}, status=status.HTTP_200_OK)
            else:
                data_serializer = UserSerializer(data=data_dict)
                if data_serializer.is_valid():
                    data_serializer.save()
                    return Response({"message": "User added successfully"}, status=status.HTTP_200_OK)
                else:
                    print(data_serializer.errors)
                    return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddFollowings(APIView):
    def post(self, request):
        try:
            data_dict = {
                "user": request.data["user"],
                "product": request.data["product"],
            }
            if User.objects.filter(email=data_dict["user"]).exists() and Product.objects.filter(id=data_dict["product"]).exists():
                if Follow.objects.filter(user=data_dict["user"], product=data_dict["product"]).exists():
                    return Response({"message": "Already following"}, status=status.HTTP_200_OK)
                else:
                    data_serializer = FollowSerializer(data=data_dict)
                    if data_serializer.is_valid():
                        data_serializer.save()
                        return Response({"message": "Followed successfully"}, status=status.HTTP_200_OK)
                    else:
                        print(data_serializer.errors)
                        return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"message": "User or product does not exist"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetProductsQuery(APIView):
    def get(self, request):
        try:
            op = request.query_params.get("type")
            query = request.query_params.get("query")
            if op == None or query == None:
                return Response({"message": "Invalid query"}, status=status.HTTP_400_BAD_REQUEST)
            elif op == "category":
                products = Product.objects.filter(category=query)
                ret = ProductSerializer(products, many=True)
                return Response(ret.data, status=status.HTTP_200_OK)
            else:
                products = Product.objects.filter(name__icontains=query)
                ret = ProductSerializer(products, many=True)
                return Response(ret.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetProduct(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs["product_id"]
            print(id)
            if Product.objects.filter(id=id).exists():
                product = Product.objects.get(id=id)
                ret = ProductSerializer(product)
                return Response(ret.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Product does not exist"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)