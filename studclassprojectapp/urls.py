# urls.py
from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDeleteView, StudentUpdateView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
]