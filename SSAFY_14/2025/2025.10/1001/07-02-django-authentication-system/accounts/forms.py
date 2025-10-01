from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreateionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = 우리의 현재 User 클래스로 대체
        # get_user)model 함수는 현재 프로젝트에서 활성화 되어있는 유저 클래스를 자동으로 반환
        model = get_user_model()