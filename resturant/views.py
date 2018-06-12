from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .form import ResturantCreateForm
# import models from databse
from .models import RestaurantLocation


# Create your views here.


# Create forms
def resturant_createview(request):
    form = ResturantCreateForm(request.POST or None)
    errors = None
    if request.method == "POST":

        form = ResturantCreateForm(request.POST)
        if form.is_valid():
            obj = RestaurantLocation.objects.create(
                name = form.cleaned_data.get('name'),
                location = form.cleaned_data.get('location'),
                category = form.cleaned_data.get('category')
            )
        return HttpResponseRedirect("/resturant/")

    if form.errros:
        errors = form.errors


    template_name = 'resturants/form.html'
    context = {"form":form, "errors":errors}
    return render(request, template_name, context)

# show database into browser
def restaurant_listView(request):
    template_name = 'resturants/restaurant_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset

    }
    return render(request, template_name, context)


# Generic base objects view
class RestuarantListView(ListView):
    template_name = 'resturants/restaurant_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset



# Detail view objects - automatically route 1 by 1 cool stuffs
class RestuarantDetailView(DetailView):
    template_name = 'resturants/resturantdetail_list.html'
    queryset = RestaurantLocation.objects.all()

    # show up page
    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id) #pk = rest_id
        return obj

# video end 2:46:24 -
# function bases views
def home(request):
    num = random.randint(0, 10000)
    some_list = [num, random.randint(0,1000), random.randint(0,1000)]
    return render(request, "base.html", { "html_content": "hi there", "num":num, "some":some_list})#response

def about(request):
    num = random.randint(0, 10000)
    some_list = [num, random.randint(0,1000), random.randint(0,1000)]
    return render(request, "about.html", { "html_content": "hi there", "num":num, "some":some_list})#response

def contact(request):
    num = random.randint(0, 10000)
    some_list = [num, random.randint(0,1000), random.randint(0,1000)]
    return render(request, "contact.html", { "html_content": "hi there", "num":num, "some":some_list})#response


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)


class home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(home, self).get_context_data(*args, **kwargs)
        print(context)
        return context

class about(TemplateView):
    template_name = 'about.html'

class ContactTemplate(TemplateView):
    template_name = 'contact.html'
