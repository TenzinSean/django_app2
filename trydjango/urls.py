"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from resturant.views import restaurant_listView


from resturant.views import (
    restaurant_listView,
    RestuarantListView,
    RestuarantDetailView,
    ResturantCreateForm

)

#from resturant.views import home, about, contact, ContactView, ContactTemplate

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^$', TemplateView.as_view(template_name='form.html')),
    url(r'^resturants/$', RestuarantListView.as_view()),
    #url(r'^resturants/(?P<slug>\w+)/$', RestuarantListView.as_view()),
    url(r'^resturants/(?P<slug>\w+)/$', RestuarantDetailView.as_view()),
    #url(r'^resturants/tibetan/$', TibetanListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    #url(r'^ContactView/$', ContactTemplate.as_view()),

]