from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Topic, Post

from django import forms


class NameForm(forms.Form):
	your_name = forms.CharField(label='お名前', max_length=30)


def index(request):
    topic_list = Topic.objects.all()
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'bbs/detail.html', {'topic': topic})

def form_page(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks_page')
    else:
        form = NameForm()
    
    return render(request, 'bbs/form_page.html', {'form': form})

def thanks_page(request):
    data = {
        'your_name': request.POST.get('your_name')
    }
    return render(request, 'bbs/thanks_page.html', {'data': data})
