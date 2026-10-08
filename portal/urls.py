from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('jobs/', views.jobs, name='jobs'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('applications/', views.my_applications, name='my_applications'),
    path('resume/', views.upload_resume, name='upload_resume'),
]