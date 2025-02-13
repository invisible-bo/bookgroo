from dotenv import load_dotenv
import os
import json
from pathlib import Path

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

# ✅ ALLOWED_HOSTS 수정 (JSON 파싱 추가)
ALLOWED_HOSTS = json.loads(os.getenv("DJANGO_ALLOWED_HOSTS", '["localhost", "127.0.0.1"]'))

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
    "rest_framework_simplejwt",
    "corsheaders",
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
}

# ✅ CORS 설정 (JSON 파싱 적용)
CORS_ALLOWED_ORIGINS = json.loads(os.getenv("DJANGO_CORS_ALLOWED_ORIGINS", '["http://localhost:3000"]'))
CORS_ALLOW_CREDENTIALS = True

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
