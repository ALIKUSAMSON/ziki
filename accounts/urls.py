from django.urls import path, reverse
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
		path('login/', accounts_views.login_view, name='login'),
		path('signup/', accounts_views.signup_view, name='signup'),

		]