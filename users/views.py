from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserCreateSerializer, UserLoginSerializer
from .logics import *
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from .doc import *


class UserAPIView(APIView):
    @swagger_auto_schema(**user_create_doc)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            if not is_email_taken(serializer.validated_data['email']):
                serializer.save()
                return Response(status=201, data=serializer.data)

            return Response(status=409, data={'error': 'email is already taken'})
        return Response(status=400)


class UserLoginAPIView(APIView):
    @swagger_auto_schema(**user_login_doc)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(status=200, data=serializer.validated_data)


@swagger_auto_schema(method='get', **is_authenticated_doc)
@api_view()
@permission_classes([permissions.IsAuthenticated, ])
def is_auth_view(request):
    return Response(status=200)


@swagger_auto_schema(method='get', **is_email_taken_doc)
@api_view()
def is_email_taken_view(request, email):
    return Response(status=200, data=is_email_taken(email))
