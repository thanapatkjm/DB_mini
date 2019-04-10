from django.urls import path, include
from . import views
from django.views.generic import TemplateView


app_name='ResRev'

urlpatterns = [
    path('', TemplateView.as_view(template_name="FrontPage.html"), name='frontPage'),
    path('register/',TemplateView.as_view(template_name="register.html"), name='register'),
	path('registering/', views.registering ,name='registering'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('new_rest/', TemplateView.as_view(template_name="new_rest.html"), name='new_rest'),
	path('add_rest/', views.add_rest ,name='add_rest'),
	path('home/', views.home, name='home'),
	path('restaurant/<int:rest_id>/add_review/', views.add_review, name='add_review'),
	path('restaurant/<int:rest_id>', views.restau , name='restau'),
]


        # <form action="{% url 'ResRev:signIn' %}" method="post">
        # {% csrf_token %}
		# <h2>Login</h1>
		# <div style="background-color:#e5e5e5;padding:15px;text-align:left;">
		# 	<input type="text" name="enter_name" placeholder="Enter your Name"><br><br>
		# 	<input type="text" name="enter_password" placeholder="Enter your Password"><br><br>
		# 	<input type="submit" value="OK">
		# </div>
        # </form>
