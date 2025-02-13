FROM python:3.11.2-slim

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# 작업 디렉토리 설정 (루트에서 시작)
WORKDIR /

# 필수 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 의존성 파일만 먼저 복사 (캐싱 활용)
COPY requirements.txt /tmp/requirements.txt

# 최신 pip + setuptools + wheel 설치
RUN pip install --upgrade pip setuptools wheel

# `pip install` 실행 (캐시 활용 가능)
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 프로젝트 전체 파일 복사 (올바른 위치 설정)
COPY . /bookgroo

# 작업 디렉토리 변경 (`manage.py`가 있는 위치)
WORKDIR /bookgroo/bookgroo

# 개발 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
