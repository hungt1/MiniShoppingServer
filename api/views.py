from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, User, Favorite, Location, Voucher
from .serializers import ProductSerializer, UserSerializer, FavoriteSerializer, LocationSerializer, VoucherSerializer
from rest_framework.parsers import JSONParser
from hashlib import sha256
from .database_helper import copy_table
from django.http import HttpResponse
from .email_handler import send
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .search import search

# Create your views here.
class ProductView(APIView):
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

    def get(self, request):
        try:
            op = request.query_params.get("type")
            query = request.query_params.get("query")
            if op == None or query == None:
                return Response({"message": "Invalid query"}, status=status.HTTP_400_BAD_REQUEST)
            elif op == "category":
                products = Product.objects.filter(category=query).values("id")
                ret = [product["id"] for product in products]
                return Response({"products": ret}, status=status.HTTP_200_OK)
            else:
                ret = search(query)
                return Response({"products": ret}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserView(APIView):
    def post(self, request):
        try:
            email = request.data["email"]
            if not User.objects.filter(email=email).exists():
                data_dict = {
                    "email": email,
                    "balance": 0.0,
                    "hash": sha256(email.encode()).hexdigest(),
                }
                data_serializer = UserSerializer(data=data_dict)
                if data_serializer.is_valid():
                    data_serializer.save()
                else:
                    print(data_serializer.errors)
                    return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            user = User.objects.get(email=email)
            data_dict = {
                "balance": user.balance,
                "hash": user.hash,
            }
            return Response({"message": "success", "data": data_dict}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

class FavoriteView(APIView):
    def post(self, request):
        try:
            hash = request.data["hash"]
            email = User.objects.get(hash=hash).email
            action = request.data["action"]
            data_dict = {
                "user": email,
                "product": request.data["product"],
            }
            if action == "add":
                if Favorite.objects.filter(user=email, product=request.data["product"]).exists():
                    return Response({"message": "Product already exists"}, status=status.HTTP_200_OK)
                data_serializer = FavoriteSerializer(data=data_dict)
                if data_serializer.is_valid():
                    data_serializer.save()
                    return Response({"message": "Product added successfully"}, status=status.HTTP_200_OK)
                else:
                    print(data_serializer.errors)
                    return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            elif action == "remove":
                if not Favorite.objects.filter(user=email, product=request.data["product"]).exists():
                    return Response({"message": "Product does not exist"}, status=status.HTTP_200_OK)
                Favorite.objects.filter(user=email, product=request.data["product"]).delete()
                return Response({"message": "Product removed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        try:
            hash = kwargs["hash"]
            user = User.objects.get(hash=hash).email
            favorites = Favorite.objects.filter(user=user).values("product")
            ret = [favorite["product"] for favorite in favorites]
            return Response({"favorites": ret}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VoucherView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            code = kwargs["code"]
            try:
                curVoucher = Voucher.objects.get(code=code)
                discount = curVoucher.discount
                quantity = curVoucher.quantity
            except:
                discount = 0
                quantity = 0
            return Response({"discount": discount, "quantity": quantity}, status=status.HTTP_200_OK)   
        except Exception as e:
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocationView(APIView):
    def post(self, request):
        try:
            hash = request.data["hash"]
            if not User.objects.filter(hash=hash).exists():
                return Response({"message": "Invalid hash"}, status=status.HTTP_400_BAD_REQUEST)
            email = User.objects.get(hash=hash).email
            location = request.data["location"]

            if not Location.objects.filter(user=email).exists():
                data_dict = {
                    "user": email,
                    "lat": location["lat"],
                    "lng": location["lng"],
                }
                data_serializer = LocationSerializer(data=data_dict)
                if data_serializer.is_valid():
                    data_serializer.save()
                    return Response({"message": "success"}, status=status.HTTP_200_OK)
                else:
                    print(data_serializer.errors)
                    return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                location_obj = Location.objects.get(user=email)
                location_obj.lat = location["lat"]
                location_obj.lng = location["lng"]
                location_obj.save()
                return Response({"message": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, *args, **kwargs):
        try:
            hash = kwargs["hash"]
            email = User.objects.get(hash=hash).email
            location = Location.objects.get(user=email)
            data_dict = {
                "lat": location.lat,
                "lng": location.lng,
            }
            return Response({"message": "success", "location": data_dict}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateDatabase(APIView):
    def get(self, request):
        try:
            copy_table("api_product", "db.sqlite3", "clone.sqlite3")
            db_file = open("clone.sqlite3", "rb")
            response = HttpResponse(db_file, content_type="application/x-sqlite3")
            response["Content-Disposition"] = "attachment; filename=db.sqlite3"
            return response
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PurchaseView(APIView):
    def post(self, request):
        try:
            hash = request.data["hash"]
            if not User.objects.filter(hash=hash).exists():
                return Response({"message": "Invalid hash"}, status=status.HTTP_400_BAD_REQUEST)
            email = User.objects.get(hash=hash).email
            rep = MIMEMultipart('mixed')
            rep.attach(MIMEText("hehehe"))
            send(rep, email)
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)