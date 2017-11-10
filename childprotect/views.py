from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
	template = loader.get_template('index.html')
	context = {
		'num_books': 5,
		'num_instances': 20,
		'num_instances_available': 35,
		'num_authors': "rahul bali",
	}
	return HttpResponse(template.render(context, request))

def login(request):
	template = loader.get_template('login.html')
	context = {}
	return HttpResponse(template.render(context, request))



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})