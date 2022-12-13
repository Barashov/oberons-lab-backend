from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserCreateSerializer
from .logics import *


class UserAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            if not is_email_taken(serializer.validated_data['email']):
                serializer.save()
                return Response(status=201, data=serializer.data)

            return Response(status=409, data={'error': 'email is already taken'})
        return Response(status=400)