from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class UserView(APIView):
    def post(self, request):
        if (
            request.data.get("username") == "admin"
            and request.data.get("password") == "admin"
        ):
            return Response({"key": "abcd"})
        return Response({"message": "username does not exist"}, status=400)
