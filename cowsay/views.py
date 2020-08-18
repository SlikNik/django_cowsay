from django.shortcuts import render
from cowsay.models import CowSay
from cowsay.forms import CowSayForm
from subprocess import check_output


def cow(text):
    cow_say = check_output(['cowsay', text]).decode("utf-8")
    return cow_say


def index(request):
    if request.method == 'POST':
        form = CowSayForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            text = form.cleaned_data.get("text")
            # output = form.get_cowsay(text)
            # print(output.stdout)
            output = cow(text)
            print(output)
            form.save()
            return render(request, 'index.html',  {'form': form,
                          'tab': 'active', 'output': output})
    form = CowSayForm()
    return render(request, 'index.html',  {'form': form, 'tab': 'active'})


def most_recent(request):
    all_cowsays = CowSay.objects.all()[::-1][:10]
    return render(request, 'most_recent.html', {'cowsays': all_cowsays, 
                  'tab': 'active'})
