from django.urls import path
from . import views
urlpatterns = [
    path('', views.QuizGame.as_view(), name='quiz'),

]
