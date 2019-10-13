from django.shortcuts import render
from . import views
from .models import Tools
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

def index(request):
    tool_list = Tools.objects.all()
    context = {
        'tool_list': tool_list,
    }

    return render(request, 'tools/index.html', context)

class CreateView(generic.CreateView):
    model = Tools
    feilds = '__all__'
    template_name = 'tools/index.html'
