from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^empresarial/new/$', views.emp_questionnaire, name='emp_questionnaire'),
    url(r'^empresarial/list/$', views.emp_list, name='emp_list')
]
