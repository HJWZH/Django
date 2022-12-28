"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views
#from .views import send_email

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #path('send_email/',send_email, name='send_email'),
    path('users/register/send_email/', views.get_name, name="send_email"),
    path('users/register/ok/', views.ok, name="ok"),
    #path('image/code/', views.img_code,name='code'),
    path('users/remove/',views.remove,name='remove'),
]
