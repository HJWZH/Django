from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import HttpResponse
from learning_log import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
def send_email(request):
    send_mail(
        subject='注册激活',
        message='我要注册激活',
        from_email=settings.EMAIL_FROM,  # 发件人
        recipient_list=['3437559454@qq.com'],  # 收件人
        #收件人可以直接写，也可以从setting.py中配置中导入
        fail_silently=False
    )
    return HttpResponse('OK')
