import os
from pathlib import Path
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 프로젝트 베이스 디렉토리 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY 설정 (환경 변수에서 가져오기)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "default-secret-key")

# OpenAI API 키
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Django가 실제 실행될 때만 WARNING 메시지 출력 (한번만 출력)
if os.environ.get("RUN_MAIN") == "true":
    if SECRET_KEY == "default-secret-key":
        print("WARNING: SECRET_KEY가 설정되지 않았습니다. 기본key를 사용합니다.")

    if not OPENAI_API_KEY:
        print("WARNING: OPENAI_API_KEY가 설정되지 않았습니다.")


# DEBUG 모드 설정
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# ALLOWED_HOSTS 설정
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# INSTALLED_APPS (추가된 앱 포함)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Django REST Framework & JWT 인증
    "rest_framework",
    "rest_framework_simplejwt",

    # CORS 설정
    "corsheaders",
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CORS 미들웨어 추가!
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

# SQLite 데이터베이스 설정 (기본값)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Django REST Framework 설정 (JWT 인증 포함)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # 기본적으로 모든 접근 허용 (추후 수정 가능)
    ],
}

# CORS 설정 (프론트엔드 연동)
CORS_ALLOW_ALL_ORIGINS = os.getenv("DJANGO_CORS_ALLOW_ALL", "False") == "True"
CORS_ALLOWED_ORIGINS = os.getenv("DJANGO_CORS_ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000").split(",")
CORS_ALLOW_CREDENTIALS = True  # 인증 정보 포함 허용

# 국제화 설정
LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

# Static & Media 설정
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []
STATIC_ROOT = BASE_DIR / "staticfiles"  # 배포 환경 대비 (현재는 사용 X)
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key 설정
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
