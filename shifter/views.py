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
            return Response(
                {
                    "token": "abcd",
                    "name": "barak",
                    "lastName": "Johnson",
                    "userId": "admin",
                    "jobDescription": "Graphic Designer",
                    "imageSrc": "Empty",
                }
            )
        return Response({"message": "username does not exist"}, status=400)


class TeamView(APIView):
    def get(self, request):
        return Response(
            {
                "employee": [
                    {
                        "imageSrc": "Empty",
                        "name": "BobBobi",
                        "lastName": "Johnson",
                        "team": "Noc Team",
                        "jobDescription": "Software Developer",
                    },
                    {
                        "imageSrc": "Empty",
                        "name": "Jane",
                        "lastName": "Smith",
                        "team": "Noc",
                        "jobDescription": "Project Manager",
                    },
                    {
                        "imageSrc": "Empty",
                        "name": "Sabrina",
                        "lastName": "Khazanov",
                        "team": "Noc",
                        "jobDescription": "Graphic Designer",
                    },
                ]
            },
            status=200,
        )


class ShiftsView(APIView):
    def get(self, request, team_id):
        if request.query_params.get("date"):
            return Response(
                {
                    "shifts": [
                        {
                            "name": "barak",
                            "start": ["2023-04-07T09:00:00", "2023-04-03T12:00:00"],
                            "end": ["2023-04-07T16:00:00", "2023-04-03T16:00:00"],
                            "color": "#f59e59",
                            "title": "barak",
                        },
                    ]
                },
                status=200,
            )
        return Response(
            {
                "shifts": [
                    {
                        "name": "barak",
                        "start": ["2023-04-14T09:00:00", "2023-04-10T12:00:00"],
                        "end": ["2023-04-14T16:00:00", "2023-04-10T16:00:00"],
                        "color": "#f59e59",
                        "title": "barak",
                    },
                    {
                        "name": "sabrina",
                        "start": ["2023-04-14T12:00:00", "2023-04-09T12:00:00"],
                        "end": ["2023-04-14T20:00:00", "2023-04-09T16:00:00"],
                        "color": "#66ffcc",
                        "title": "sabrina",
                    },
                    {
                        "name": "koko",
                        "start": ["2023-04-13T09:00:00"],
                        "end": ["2023-04-13T16:00:00"],
                        "color": "#00cc66",
                        "title": "koko",
                    },
                    {
                        "name": "chiko",
                        "start": ["2023-04-12T09:00:00"],
                        "end": ["2023-04-12T16:00:00"],
                        "color": "#FFC107",
                        "title": "chiko",
                    },
                ]
            },
            status=200,
        )
