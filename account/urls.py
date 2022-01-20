from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'user'

urlpatterns = [

	# register user
	path('register' , views.register, name='register'),

	# login user
	path('login', views.login_user, name='login' ),
	
	#  logout user
	path('logout', views.logout_user, name='logout'),
    # path('logout', views.logout, name='logout'),





]
