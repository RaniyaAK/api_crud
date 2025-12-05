from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('api/all_students',views.student_details, name="student_details"),
    path ('api/add_students',views.add_student_details, name="add_student_details"),
    path ('api/update_student/<int:student_id>',views.update_student_details, name="update_student_details"),
    path ('api/delete_student/<int:student_id>',views.delete_student_details, name="delete_student_details"),
]