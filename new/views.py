from django.shortcuts import render
from rest_framwork.veiws import APIView
from rest_framwork.response import Response
# Create your views here.
class HelloapiView(APIView):
    """
    This is the api view for hello api
    """
    def get(self, request, format=None):
        an_apiview = [

        ]
        return Response({'hello':'world'})