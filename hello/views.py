from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            context = {'form': form, 'name': form['name'].value()}

    else:
        form = NameForm()
        context = {'form': form}

    return render(request, 'index.html', context)