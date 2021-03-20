from django.urls import path

from adminapp.views import index, UserListView, UserCreateView,\
    UserUpdateView, UserDeleteView, admin_products, admin_products_create,\
    admin_products_update, admin_products_delete

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products/', admin_products, name='admin_products'),
    path('products-create/', admin_products_create, name='admin_products_create'),
    path('products-update/<int:product_id>/', admin_products_update, name='admin_products_update'),
    path('products-delete/<int:product_id>/', admin_products_delete, name='admin_products_delete'),
]