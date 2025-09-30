from django import forms
from .models import Article

# DB에 연동할 것이기 때문에 모델 폼?
class ArticleForm(forms.ModelForm):
    # 내가 적용하고 싶은 모델을 알려줘야 함
    class Meta:
        model = Article
        fields = '__all__'