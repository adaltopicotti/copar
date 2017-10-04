from django.conf.urls import url, includes
from . import views

urlpatterns = [
    url(r'^$', views.questionnaire, name='questionnaire'),
]
