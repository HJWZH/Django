from django import forms

from .models import Topic, Entry

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
        username = forms.CharField(label="用户名称",widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入注册用户名称'}))
        age = forms.CharField(label="邮箱",widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱号'}))
        status = forms.CharField(label="密码(大于8位数且必须包含大小写)",widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入注册用户密码'}))