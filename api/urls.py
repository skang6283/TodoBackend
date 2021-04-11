from django.urls import path, include
from . import views


urlpatterns=[
    path('intermediate/', views.IntermediateList.as_view()),
    path('goal/', views.GoalList.as_view()),

    path('intermediate/<str:pk>/', views.IntermediateDetail.as_view()),
    path('goal/<str:pk>/', views.GoalDetail.as_view()),
]
