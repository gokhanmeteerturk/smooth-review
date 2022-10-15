from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload/', views.ReviewSubmissionView.as_view(), name='review_submission'),
]
