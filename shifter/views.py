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
            return Response({{"token": "abcd"},{"name": "BobBobi"},{"lastName":"Johnson"},{"userId":"admin"},{"jobDescription":"Graphic Designer"},{"imageSrc": "Empty"}})
        return Response({"message": "username does not exist"}, status=400)


class TeamView(APIView):
    def get(self, request):
        return Response(
            {
                "employee": [
                    {
                        "imageSrc": "Empty",
                        "name": "John Doe",
                        "jobDescription": "Software Developer",
                    },
                    {
                        "imageSrc": "Empty",
                        "name": "Jane Smith",
                        "jobDescription": "Project Manager",
                    },
                    {
                        "imageSrc": "Empty",
                        "name": "BobBobi Johnson",
                        "jobDescription": "Graphic Designer",
                    },
                ]
            },
            status=200,
        )
