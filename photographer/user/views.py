from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.models import Address,User
from .forms import RegisterForm,LoginForm,ProfileForm,PartialProfileForm,PartialUserProfileForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.conf import settings

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            #user_cart = Cart(user = form.)
            return redirect(settings.LOGIN_REDIRECT_URL)

    else:
        form = RegisterForm()

    return render(response,  "user/user.html", {"form":form})

def login(request):
    current_user = request.user
    if request.method == 'POST':
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f' welcome {username} !!')
            try:
                if request.GET['next']:
                    return redirect(request.GET['next'])
            except Exception as e:
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.info(request, f'account does not exist plz sign in')
    form = LoginForm()
    return render(request, 'user/user.html', {'form':form})

@login_required
def profileaddress(request):
    current_user = request.user

    if request.method == 'POST':
        item = Address.objects.filter(user = current_user)
        if item.exists():
            form = PartialProfileForm(request.POST, instance = item[0])
        else:
            form = PartialProfileForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = current_user
            address.save()
            return render(request, 'user/profileaddress.html', {'form':form})
        else:
            messages.info(request, f'account does not exist plz sign in')

    form = PartialProfileForm()
    item = Address.objects.filter(user=current_user)
    if item.exists():
        form = PartialProfileForm(instance = item[0])

    return render(request, 'user/profileaddress.html', {'form':form})

@login_required
def userprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = PartialUserProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = current_user
            address.save()
            # return redirect("user/userprofile.html")
            return render(request, 'user/userinformation.html', {'form':form})
        else:
            messages.info(request, f'account does not exist plz sign in')

    form = PartialUserProfileForm()
    item = User.objects.filter(id=current_user.id)
    if item.exists():
        form = PartialUserProfileForm(instance = item[0])
    return render(request, 'user/userinformation.html', {'form':form})

