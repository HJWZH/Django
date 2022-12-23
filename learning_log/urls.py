from django.contrib import admin
from django.urls import path, include
from users import views
from django.views.static import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
    #path('send_email/', views.send_email, name="send_email")
]
