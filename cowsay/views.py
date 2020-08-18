from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from cowsay.models import CowSay
from cowsay.forms import CowSayForm


def index(request):
    if request.method == 'POST':
        form = CowSayForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            text = form.cleaned_data['text']
            output = form.get_cowsay(text)
            print(output)
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = CowSayForm()
    return render(request, 'index.html',  {'form': form, 'tab': 'active'})


def most_recent(request):
    all_cowsays = CowSay.objects.all()[::-1][:10]
    return render(request, 'most_recent.html', {'cowsays': all_cowsays, 'tab': 'active'})
