from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "password", "email","nickname"] 

        extra_kwargs = {
            "password": {"write_only": True} 
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
