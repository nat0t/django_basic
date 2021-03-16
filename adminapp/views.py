from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import ShopUser as User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm,\
    ProductAdminCreationForm
from mainapp.models import Product

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')

# READ
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)

# CREATE
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)

# UPDATE
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES,
                                    instance=user)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {'form': form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)

# DELETE
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_delete_restore(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = not user.is_active
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'adminapp/admin-products-read.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = ProductAdminCreationForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-create.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductAdminCreationForm(data=request.POST, files=request.FILES,
                                    instance=product)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = ProductAdminCreationForm(instance=product)
    context = {'form': form, 'product': product}
    return render(request, 'adminapp/admin-products-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_products'))