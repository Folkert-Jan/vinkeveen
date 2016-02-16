from django.shortcuts import render

# Create your views here.
from .forms import TrainingenForm
from training.models import Trainingen

def Trainingen_function(request):
	title = "mytitle"
	form = TrainingenForm(request.POST or None)	


	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form = TrainingenForm()

	Trainingen = Trainingen.objects.all()
	Trainingen.Print()


	context = {
		"template_title": title,
		"form" : form, 
		"Trainingen" : trainingen,	
	}



	return render(request, "Training.html" , context)
