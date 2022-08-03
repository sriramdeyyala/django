from django.shortcuts import render
from .serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
User = get_user_model()
from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse


# log in form
class LoginView(generics. GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.authenticate()
        print(user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'key': token.key, 'details': UserDetailSerializer(user, context={'request':request}).data}, status=status.HTTP_200_OK)


# logout form
class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'details':'logout succesfully'}, status=status.HTTP_200_OK)


# register
class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email)
        return Response({'details':'user is created'},status=status.HTTP_200_OK)








# # model view
#
# class UserModelView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class = ModelDetailSerializer
#
#
#
#
#     serializer_class = OrganizationSerializer

# class UserOrganization(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#
#     def get_queryset(self):
#         organization = get_object_or_404(Organization, id=self.kwargs.get('organization_id'))
#         query_set = self.queryset(organization=organization)
#         return query_set
#
#     def perform_create(self, serializer):
#         organization = get_object_or_404(Organization, id=self.kwargs.get('organization_id'))
#         serializer.save(organization=organization)


# # get
#
# class UserList(APIView):
#     def get(self, request, id=None):
#         if id:
#             item = User.objects.get(id=id)
#             serializer = OrganizationSerializer(item)
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#
#         items = User.objects.all()
#         serializer = OrganizationSerializer(items, many=True)
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200)
#
# #create
# class Usercreate(APIView):
#     def post(self, request):
#         serializer = OrganizationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#
# # update
# class Usermodify(APIView):
#     def patch(self, request, id=None):
#         item = User.objects.get(id=id)
#         serializer = OrganizationSerializer(item, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})
#         else:
#             return Response({"status": "error", "data": serializer.errors})
#
#
# #delete
#
# class UserDelete(APIView):
#     def delete(self, request, id=None):
#         item = get_object_or_404(User, id=id)
#         item.delete()
#         return Response({"status": "success", "data": "Item Deleted"})


