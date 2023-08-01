from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students),
    path('student/<id>/', views.student_),
    path('student-update/', views.student_update),
    path('student-delete', views.student_delete),
    path('student-create', views.student_create),
]