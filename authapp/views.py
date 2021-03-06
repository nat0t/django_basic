from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'authapp/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES,
                               instance=request.user)
        if form.is_valid:
            form.save()
            messages.success(request, 'Профиль успешно изменён.')
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_price = sum(
        basket.quantity * basket.product.price for basket in baskets)

    context = {'form': form,
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_price': total_price,
               }
    return render(request, 'authapp/profile.html', context)