from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^empresarial/new/$', views.questionnaire_emp, name='questionnaire_emp'),
]
