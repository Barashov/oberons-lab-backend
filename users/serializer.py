from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(email=email,
                                        password=password)

        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

