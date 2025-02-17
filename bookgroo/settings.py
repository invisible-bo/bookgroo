from dotenv import load_dotenv
import os
import json
from pathlib import Path
from datetime import timedelta

# .env 파일 로드
load_dotenv()

# 프로젝트 베이스 디렉토리 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY 설정
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "default-secret-key")

# SECRET_KEY가 없거나 기본값이면 경고 출력
if not SECRET_KEY or SECRET_KEY == "default-secret-key":
    print("WARNING: SECRET_KEY가 설정되지 않았습니다. 기본 key를 사용합니다.")

# OpenAI API 키
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY and not os.environ.get("OPENAI_WARNING_SHOWN"):
    print("<<<<<<<<<<<<<<<<<<<<<<")
    print("WARNING: OPENAI_API_KEY가 설정되지 않았습니다.")
    print(">>>>>>>>>>>>>>>>>>>>>>")
    os.environ["OPENAI_WARNING_SHOWN"] = "True"  # 경고 메시지 한 번만 출력

# DEBUG 모드
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# ALLOWED_HOSTS (VITE 개발서버와 외부 접속 IP 추가)
ALLOWED_HOSTS = json.loads(
    os.getenv(
        "DJANGO_ALLOWED_HOSTS", '["localhost", "127.0.0.1", "0.0.0.0", "211.38.232.27"]'
    )
)

# INSTALLED_APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 추가된 앱
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    # local apps (추가)
    "accounts",
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ROOT URL 설정
ROOT_URLCONF = "bookgroo.urls"

# TEMPLATES 설정
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI 설정
WSGI_APPLICATION = "bookgroo.wsgi.application"

# AUTH_USER_MODEL 추가
AUTH_USER_MODEL = "accounts.User"

# SQLite 데이터베이스 설정 (CONN_MAX_AGE 추가)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "CONN_MAX_AGE": 600,
    }
}

# Django REST Framework 설정 (JWT 포함)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# JWT 설정 (유효기간 및 Refresh Rotation)
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# CORS 설정 (JSON 파싱 적용, VITE 개발서버와 외부 접속 IP 추가)
CORS_ALLOWED_ORIGINS = json.loads(
    os.getenv(
        "DJANGO_CORS_ALLOWED_ORIGINS",
        '["http://localhost:3000", "http://localhost:5173", "http://211.38.232.27:5173"]',
    )
)
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_HEADERS (CSRF 문제 발생 시 필요)
CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# 국제화 설정
LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

# Static & Media 설정
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key 설정
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#이메일 인증
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")