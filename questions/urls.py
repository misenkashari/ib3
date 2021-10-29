from django.urls import path
from .views import *


app_name = 'questions'

urlpatterns = [
    path('', QuestionListView.as_view(), name='index'),
    path('create/', QuestionCreateView.as_view(), name='create'),
    path('like/<int:pk>', LikeView, name='like'),
    path('<int:pk>/details/', QuestionDetailView.as_view(), name='details'),
    path('<int:pk>/answer', CommentView.as_view(), name='answer'),
    path('<int:pk>/likeanswer', LikeAnswer, name='like-answer'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('<int:pk>/delete/', question_delete, name='delete'),
    path('<int:pk>/update/', QuestionUpdateView.as_view(), name='update')
]