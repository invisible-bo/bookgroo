import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookgroo.settings")
django.setup()

from accounts.models import Genre

genres = [
    "소설",
    "에세이 시",
    "경제 경영",
    "자기계발",
    "인문",
    "사회 정치",
    "역사",
    "종교",
    "예술 대중문화",
    "자연과학",
    "가정 살림",
    "건강 취미 여행",
    "어린이 유아",
    "청소년",
    "국어 외국어",
    "IT 모바일",
    "대학교재",
    "수험서 자격증",
    "잡지",
    "만화",
    "로맨스",
    "판타지/무협",
]

for genre in genres:
    Genre.objects.get_or_create(name=genre)

print("장르 데이터 추가 완료!")
