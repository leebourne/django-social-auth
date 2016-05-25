from django.conf.urls import url
import views

urlpatterns = [ 
    url(r'^require_company$', views.require_company, name='require_company'),
    ]
