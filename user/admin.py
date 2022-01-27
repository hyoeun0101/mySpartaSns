from django.contrib import admin
from .models import UserModel  # 생성한 모델 가져오기
# .models에서  .은 지금 위치와 동일한 곳에서 models 불러오겠다는 뜻

# Register your models here.
admin.site.register(UserModel)
# 가져온 UserModel 을 관리자 페이지에 넣어주겠다==나의 UserModel 을 Admin에 추가

