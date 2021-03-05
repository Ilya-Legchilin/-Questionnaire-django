from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),              
   path('quests', views.quests, name='quests'),     
   path('storage', views.storage, name='storage'),
   path('quests/<int:pk>/', views.quest_pass, name='quest-pass'),
   path('receive_record', views.receive_record, name='receive-record')
]
