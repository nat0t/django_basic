from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import ShopUser as User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm,\
    ProductAdminCreationForm
from mainapp.models import Product

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    context = {'title': 'GeekShop - Админка'}
    return render(request, 'adminapp/index.html', context)

# READ
class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

# CREATE
class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin-staff:admin_users')
    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

# UPDATE
class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admin_staff:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

# DELETE
class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

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