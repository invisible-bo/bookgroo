import uuid
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import EmailMessage
from .models import User, Genre
from .serializers import UserSerializers,GenreSerializer
from .utils import EmailThread

class GenreListView(APIView):
    permission_classes = [AllowAny]  # 인증 없이 누구나 접근 가능

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class UserList(APIView):
    """
    List all Users or create a new User with email verification
    """

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [AllowAny()]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        preferred_genres_ids = request.data.pop("preferred_genres", [])
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            genres = Genre.objects.filter(id__in=preferred_genres_ids) #선택한 장르 저장
            user.preferred_genres.set(genres)

            user.is_active = False
            user.activation_token = str(uuid.uuid4())  # 이메일 인증 토큰 생성
            user.save()

            activation_link = f"http://127.0.0.1:8000/api/v1/accounts/emailauth/{user.activation_token}/"
            email_subject = "이메일 인증 요청"
            email_body = f"아래 링크를 클릭하여 이메일 인증을 완료하세요:\n{activation_link}"

            print(f"user이메일 {user.email}") 
            print(f"인증링크 {activation_link}") 

            email = EmailMessage(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
            EmailThread(email).start()

            return Response(
                {"message": "회원가입이 완료되었습니다. 이메일 인증을 진행해주세요."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#이메일 인증-사용자가 이메일에서 링크 클릭하면 작동하는 코드드
class ActivateAccountView(APIView):
    def get(self, request, token):
        try:
            user = User.objects.filter(activation_token=token).first()
            if user is None:
                return Response(
                    {"message": "db에 없는 토큰입니다다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if user.is_active:
                return Response(
                    {"message": "이미 이메일 인증이 완료된 계정입니다"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.is_active = True
            user.activation_token = None  # 토큰 초기화
            user.save()

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            response = Response(
                {
                    "user": UserSerializers(user).data,
                    "message": "이메일 인증이 완료되었습니다. 자동 로그인 되었습니다!",
                    "jwt_token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)

            return response

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a User instance
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    # 유저 상세정보 조회
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializers(user)
        return Response(serializer.data)

    # 유저 정보 수정
    def put(self, request, pk):
        user = self.get_object(pk)
        preferred_genres_ids = request.data.pop("preferred_genres", None)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #선택한 장르 업데이트
            if preferred_genres_ids is not None:
                genres = Genre.objects.filter(id__in=preferred_genres_ids)
                user.preferred_genres.set(genres)
                
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 계정 삭제
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 아이디, 비번이 맞으면 JWT 발급
class UserLogin(APIView):
    """
    If the User credentials (Username, password) are valid, an access token and a refresh token will be issued.
    """

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.filter(username=username).first()

        if user is None:
            return Response(
                {"message": "존재하지 않는 아이디입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not check_password(password, user.password):
            return Response(
                {"message": "비밀번호가 맞지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if not user.is_active:
            return Response(
                {"message": "이메일 인증이 필요합니다! 이메일을 확인하세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token = TokenObtainPairSerializer.get_token(user)  # refresh 토큰 생성
        refresh_token = str(token)  # refresh 토큰 문자열화
        access_token = str(token.access_token)  # access 토큰 문자열화
        
        response = Response(
            {
                "user": UserSerializers(user).data,
                "message": "login success",
                "jwt_token": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                },
            },
            status=status.HTTP_200_OK,
        )

        response.set_cookie("access_token", access_token, httponly=True)
        response.set_cookie("refresh_token", refresh_token, httponly=True)

        return response 


# 로그아웃
class UserLogout(APIView):
    """
    The refresh token will be added to the blacklist, and token data in cookies and sessions will be removed
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response(
                    {"message": "토큰이 없어용"}, status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            response = Response(
                {"message": "로그아웃 되었습니다."}, status=status.HTTP_200_OK
            )
            response.delete_cookie("refresh_token")
            response.delete_cookie("access_token")

            return response
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
