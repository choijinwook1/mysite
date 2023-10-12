from django import forms
from pybo.models import Product, Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class ProductForm(forms.ModelForm): # ModelForm 은 장고 모델 폼
    class Meta: # 장고 모델 폼은 반드시 내부에 Meta 클래스 가져야 함
        model = Product
        fields = ['pcode', 'pname', 'unitprice', 'discountrate', 'mainfunc', 'detailfunc', 'imgfile']
        labels = {
            'pcode': '제품 코드 ',
            'pname': '제 품 명 ',
            'unitprice': '단    가 ',
            'discountrate': '할 인 율 ',
            'mainfunc': '주요 기능',
            'detailfunc': '상세 기능',
            'imgfile': '이 미 지'
        }