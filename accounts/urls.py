from django.urls import path, include
from . import views #importing views from current directory means accounts.
urlpatterns = [
			path('signup/', views.signup, name = 'signup'), #if someone puts accounts/signup
			path('login/', views.login, name = 'login'),    #if someone puts accounts/login
			path('logout', views.logout, name = 'logout'),  #if someone puts accounts/logout

]