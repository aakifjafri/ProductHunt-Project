
from django.contrib import admin
from django.urls import path, include
from products import views  # we did this because we want to show views of products as hoempage.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('accounts/', include('accounts.urls')), #anything that has accounts/ its takes it to urls.py of accounts.
]
