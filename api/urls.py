from django.urls import path
from .views import QuestionList, QuestionDetail

urlpatterns = [
    path("questions/", QuestionList.as_view(), name="question_list"),
    path("questions/<int:pk>/", QuestionDetail.as_view(), name="question_detail")
]
