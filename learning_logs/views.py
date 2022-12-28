from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.contrib import messages
from django import forms as djforms
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.core.mail import send_mail
from django.shortcuts import HttpResponse
from learning_log import settings
from .forms import NameForm
from django.http import HttpResponseRedirect
from .forms import NameForm,USERSREMOVE
from django.contrib.auth.models import User
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    #if topic.owner != request.user:
        #raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #if topic.owner != request.user:
        #raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)



def get_name(request):
    if request.method == 'POST':
        # 如果这个表单是post请求，我们需要处理数据
        form = NameForm(request.POST)
        if form.is_valid():  # 检查界面是否传入表单数据
            # 表单数据被存储在 form.cleaned_data 中
            return HttpResponseRedirect('/thanks/')  # 返回一个界面，输入该界面的URL
    else:
        # 如果是一个get请求，将创建一个空表单
        form = NameForm()
    return render(request, 'learning_logs/name.html', {'form': form})

def ok(request):
    a,b,c=NameForm(request.POST)
    try:
        send_mail(
            subject='注册激活',
            message=f'我要注册激活\n用户名：{a}\n邮箱：{b}\n密码：{c}',
            from_email=settings.EMAIL_FROM,  # 发件人
            recipient_list=['3437559454@qq.com'],  # 收件人
            #收件人可以直接写，也可以从setting.py中配置中导入
            fail_silently=False
        )
    except:
        return HttpResponse('网络问题，无法提交！请手动提交申请到:3437559454@qq.com[标题写注册激活，备注好用户名，邮箱号，密码(大于8位数且必须包含大小写)]，审核结果会发送到你的邮箱上！')
    else:
        return HttpResponse('提交成功！\n请等待审核……\n审核结果会发送到你的邮箱上！')
@login_required
def remove(request):
    if request.method == 'POST':
        # 如果这个表单是post请求，我们需要处理数据
        forms = USERSREMOVE(request.POST)
        if forms.is_valid():  # 检查界面是否传入表单数据
            # 表单数据被存储在 form.cleaned_data 中
            for key in request.POST:
                a=request.POST.get(key)
            try:
                User.objects.get(username=str(a)).delete()
            except:
                return HttpResponse(f'没有此用户！')
            else:
                return HttpResponse(f'{a}已被删除!')  # 返回一个界面，输入该界面的URL
    else:
        if request.user.username != "wangziheng":
            return HttpResponse(f'权限不足！！！仅限管理员HJ(WZH)可更改！！！')
        # 如果是一个get请求，将创建一个空表单
        else:
            forms = USERSREMOVE()
            return render(request, 'learning_logs/remove-list.html', {'forms': forms})
def test(request):
        user=User.objects.all()
        num=len(User.objects.all())
        b=[]
        for i in range(num):
            a=user[i].username
            b.append(a)
        messages.success(request,f'目前用户:{b}')