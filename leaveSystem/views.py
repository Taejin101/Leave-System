from unicodedata import name
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from leaveSystem.models import account_data
import random
from django.core.mail import send_mail, EmailMultiAlternatives
from .forms import applicationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from . import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

applications = {}

def index(request):
    # redirect to respective roles based on their roles
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.user.role.name == "admin":
        return redirect('admin/')
    elif request.user.role.name == "staff":
        return redirect('staff/')
    else:
        return redirect('student/')
    # return HttpResponseRedirect(reverse("application"))

@login_required(login_url="login")
def deleteSessionOrAccountData(request, key):
    if request.user.is_authenticated:
        username = request.user.username
        account_data.objects.filter(username=username).delete()
    else:
        del request.session[key]

# for login purpose
def login_view(request):
    if request.method == "POST":
        # fetch post data
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check if user exists
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Invalid email")
            return redirect(reverse("login"))

        # authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # user is authenticated creating session using login
            login(request, user)
            # redirect to index
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, "leaveSystem/login.html")
    else:
        return render(request, "leaveSystem/login.html")

# for logout purpose
@login_required(login_url="login")
def logout_view(request):
    # logout and delete session
    logout(request)
    return HttpResponseRedirect(reverse("login"))

# application form
@login_required(login_url="login")
def application(request):
    if request.method=="POST":
        # post request 

        # create application resource in db
        Application.objects.create(username=request.user.username, rollno = request.POST.get('rollno'), phoneno = request.POST.get('phoneno'), fatherName = request.POST.get('fatherName'), branch = request.POST.get('branch'), semester = request.POST.get('semester'), hostelNumber = request.POST.get('hostelNumber'), roomNumber = request.POST.get('roomNumber'), fromDate = request.POST.get('fromDate'), time = request.POST.get('time'), toDate = request.POST.get('toDate'), reason = request.POST.get('reason'), parentContact = request.POST.get('parentContact'), role = request.user.role)

        return HttpResponseRedirect(reverse("applicationView"))
    else:
        return render(request, "leaveSystem/application.html", {
            "form": applicationForm()
        })

@login_required(login_url="login")
def application_view(request):
        # fetch self applications
        queryset = pending_requests(request.user.username)

        # render applications page
        return render(request, "leaveSystem/application_view.html", {
            "applications" : queryset
        })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def application_requests(request):
    if len(applications) > 0:
        return render(request, "leaveSystem/application_requests.html", {
            'application': applications
        })
    else:
        return render(request, "leaveSystem/application_requests.html")

@login_required
@user_passes_test(lambda u: u.is_superuser)
def respond_requests(request, id, is_approved):
    if id in applications:
        # print(applications[id])
        applications[id]['status'] = is_approved
        email=applications[id]['email']
        name=applications[id]['name']
        rollno=applications[id]['rollno']
        phoneno=applications[id]['phoneno']
        fatherName=applications[id]['fatherName']
        branch=applications[id]['branch']
        semester=applications[id]['semester']
        hostelNumber=applications[id]['hostelNumber']
        roomNumber=applications[id]['roomNumber']
        fromDate=applications[id]['fromDate']
        time=applications[id]['time']
        toDate=applications[id]['toDate']
        reason=applications[id]['reason']
        parentContact=applications[id]['parentContact']
        status="Approved" if applications[id]['status'] == 1 else "Rejected"

        # We can save approved or rejected requests here
        f = applicationModel(name=name, rollno=rollno, phoneno=phoneno, fatherName=fatherName, branch=branch, semester=semester, hostelNumber=hostelNumber, roomNumber=roomNumber, fromDate=fromDate, time=time, toDate=toDate, reason=reason, parentContact=parentContact, status=status)
        f.save()
        # Mail service can also be provided here
        message = f'Your leave application from {fromDate} to {toDate} has been {status}'
        send_mail(
            'Leave Application',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        applications.pop(id)
        return HttpResponse("True")
    else:
        return HttpResponse("Error")
    
def parent_confirmation(request):
    id = int(request.GET.get('id'))
    action = bool(request.GET.get('action'))
    if id in applications:
        print("parent response recorded")
        applications[id]['parent_responded'] = True
        applications[id]['parent_response'] = action
    return HttpResponse("Your Response is recorded")
