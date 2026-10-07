from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout

from .models import StudentProfile,Job,Application


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('register')

        if StudentProfile.objects.filter(roll_number=roll_number).exists():
            messages.error(request, 'Roll number is already registered.')
            return redirect('register')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        StudentProfile.objects.create(
            user=user,
            phone=phone,
            department=department,
            roll_number=roll_number
        )

        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')

        messages.error(request, 'Invalid email or password.')
        return redirect('login')

    return render(request, 'login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    student = StudentProfile.objects.get(user=request.user)

    return render(request, 'dashboard.html', {
        'student': student
    })
def logout_view(request):
    logout(request)
    return redirect('home')
def jobs(request):
    if not request.user.is_authenticated:
        return redirect('login')

    job_list = Job.objects.all()

    return render(request, 'jobs.html', {
        'jobs': job_list
    })   
def apply_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')

    job = Job.objects.get(id=job_id)

    Application.objects.get_or_create(
        student=request.user,
        job=job
    )

    messages.success(request, 'Application submitted successfully!')
    return redirect('jobs')
def my_applications(request):
    if not request.user.is_authenticated:
        return redirect('login')

    applications = Application.objects.filter(
        student=request.user
    ).select_related('job')

    return render(request, 'applications.html', {
        'applications': applications
    })