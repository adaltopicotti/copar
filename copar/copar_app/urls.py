from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^empresarial/new/$', views.emp_questionnaire, name='emp_questionnaire'),
    url(r'^empresarial/list/$', views.emp_list, name='emp_list'),
    url(r'^empresarial/detail/(?P<pk>[0-9]+)/$', views.emp_detail, name='emp_detail')
]
