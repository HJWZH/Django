from django import forms

from .models import Topic, Entry
from django.contrib.auth.models import User
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
class NameForm(forms.Form):
        username = forms.CharField(label="用户名称",required=True,widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入注册用户名称'}))
        age = forms.EmailField(label="邮箱",widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱号'}))
        status = forms.CharField(required=True,label="密码(大于8位数且必须包含大小写)",widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入注册用户密码'}),min_length=8)

class USERSREMOVE(forms.Form):
    user=User.objects.all()
    num=len(User.objects.all())
    b=[]
    for i in range(num):
        a=user[i].username
        b.append(a)
    choice = forms.ChoiceField(label='选择模式',choices=(
        ("2","开始删除用户"),
    ))
    
    usernames = forms.CharField(required=True,label=f"目前用户：{b}",widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入要删除的用户'}))