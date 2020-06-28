from django.shortcuts import render

from first_app.models import *
from first_app import forms
from first_app import modelsforms

## FOR LOGIN ##################################################
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# Views:

def index(request):
    return render(request,template_name='index.htm')



@login_required
def topicTable(request):
    access_records = AcessRecords.objects.all()
    context = {'access_records':access_records}
    return render(request,template_name='topictable.htm',context=context)



def ViewForm(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something with data
            print("Data Validated")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
            
    return render(request,'forms.htm',context={'form':form})


#_______________________________________________________________________________________________   
#
#                           FOR REGISTRATION & LOGIN 
#_______________________________________________________________________________________________


def NewUser(request):
    if request.method == "POST":
        mf_userForm = modelsforms.UserForm(request.POST)
        mf_userInfoForm = modelsforms.UserProfileInfoForm(request.POST)

        # print(mf_userForm)
        # print(mf_userInfoForm)
        if mf_userForm.is_valid() and mf_userInfoForm.is_valid():

            ## Saving User Form********************************
            user = mf_userForm.save()
            user.set_password(user.password)
            user.save()
            ## Saving Pofile Info Form*************************
            profile = mf_userInfoForm.save(commit=False)
            profile.user = user
            
            print(request.FILES)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
            # return index(request)
        else:
            print("Form Invalid!")
            print(mf_userForm.errors)
            print(mf_userInfoForm.errors)
            registered = False
    else:
        mf_userForm = modelsforms.UserForm()
        mf_userInfoForm = modelsforms.UserProfileInfoForm()
        registered = False

    print(f"-----Reg: {registered}------")
    return render(request,'registration.htm',context={'Userform':mf_userForm,'UserProfileInfoForm':mf_userInfoForm, 'registered':registered})



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)

        print(f"User: {user}")

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('first_app:Index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print(f"Login Failed [{username}:{password}]")
            return HttpResponse("Invalid user details.")
    
    else:
        return render(request,'login.htm',context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:Index'))