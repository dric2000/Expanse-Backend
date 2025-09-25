from django.shortcuts import render
from rest_framework import generics
from .models import * 
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class TransactionListCreateView(generics.ListCreateAPIView): 
  permission_classes = [IsAuthenticated]
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer
  lookup_field = "id"



class UserListCreateView(generics.ListCreateAPIView): 
  #permission_classes = [IsAuthenticated]
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = "id"


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer