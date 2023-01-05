from django.shortcuts import render,redirect
from .forms import (
    SingUpForm,
    LoginForm,
    UserProfileUpdateForm,
    ProfilePictureUpdateForm
)
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .decorators import(
    not_logged_in_required
)
from django.contrib.auth import login,logout, authenticate
from django.shortcuts import get_object_or_404

from .models import (
    User
)



#sing up
@never_cache
@not_logged_in_required
def SingUp(request):

    form = SingUpForm()

    if request.method == "POST":
        form = SingUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))

            user.save()
            messages.success(request, "Registrations Successfully done!")
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
            return redirect("siungIn")

        else:
            print("_______________________________________________________________________________________")
            print(form.errors)
    context = {
        "form": form,
    }
    return render(request, 'singUp.html', context)


#sing in
def SingIn(request):

    login_form = LoginForm()

    try:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(
                    username=login_form.cleaned_data.get('username'),
                    password=login_form.cleaned_data.get('password')
                )
                if user:
                    login(request, user)
                    return redirect("/") 

                else:
                    messages.warning(request, "You've given wrong information, try again!") 
                    return redirect("siungIn") 
    except:
        messages.warning(request, "You've given wrong information, try again!")   
        return redirect("siungIn")
    context = {

    }
    return render(request, 'singIn.html', context)

#logout
@never_cache
def Logout(request):
    logout(request)
    return redirect("/")

#profile
@login_required(login_url='siungIn')  
def Dashboard(request):

    account = get_object_or_404(User, pk=request.user.pk)

    form = UserProfileUpdateForm(instance=account)
    if request.method == "POST":
        if request.user.pk != account.pk:
            redirect("/")
        form = UserProfileUpdateForm(request.POST, instance=account)  

        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated.")
            
            return redirect("Dashboard")
        else:
            #messages.warning(request, form.errors)
            print(form.errors)

    context = {
        "account":account, 
        "form":form,
    } 

    return render(request, 'dashboard.html',context)


@login_required(login_url='siungIn')  
def ChangeProfilePicture(request):
    if request.method == "POST":
        form = ProfilePictureUpdateForm(request.POST, request.FILES)
        if form.is_valid():

            image = request.FILES['profile_image']
            user = get_object_or_404(User, pk=request.user.pk)

            print("-------------------------------------------------------------")

            if request.user.pk != user.pk:
                return redirect("Dashboard")

            user.profile_image = image
            user.save()
            messages.success(request,"Profile picture update success!")

    return redirect('Dashboard') 
   

