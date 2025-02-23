from .models import User, Genre
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

class UserSerializers(serializers.ModelSerializer):
    preferred_genres = GenreSerializer(many=True, read_only=True) 
    preferred_genres_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    ) 

    class Meta:
        model = User
        fields = ["username", "password", "email", "nickname", "preferred_genres", "preferred_genres_ids"]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        genre_ids = validated_data.pop("preferred_genres_ids", [])  # 장르 ID 리스트 추출
        validated_data["password"] = make_password(validated_data["password"])  # 비밀번호 암호화
        
        user = super().create(validated_data)  
        user.preferred_genres.set(Genre.objects.filter(id__in=genre_ids))  
        return user

    def update(self, instance, validated_data):
        genre_ids = validated_data.pop("preferred_genres_ids", None)
        
        instance = super().update(instance, validated_data)  
        
        if genre_ids is not None:
            instance.preferred_genres.set(Genre.objects.filter(id__in=genre_ids))  

        return instance
