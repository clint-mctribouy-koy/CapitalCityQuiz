
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
import random
from django.template import loader
from django.contrib import messages

from .models import Quiz


from .forms import QuizForm
from django.views.generic import View

# Create your views here.
class QuizGame(View):
    def post(self, request):
        if request.method == 'POST':
            all_countries = {}
            url = 'https://countriesnow.space/api/v0.1/countries/capital'
            response = requests.get(url)
            data = response.json()
            countries = data['data']
            for i in countries:
                quiz_data = Quiz(country = i['name'], capital_city = i['capital'])
                quiz_data.save()
            
                all_countries = Quiz.objects.all()
            
            form = QuizForm

            random_country = random.sample(list(all_countries), 1)
            input_answer = request.POST.get('capital_city_field').capitalize()
            correct_answer = request.POST.get('question')
            


            if input_answer:
                if input_answer == correct_answer:
                    messages.success(request,"WELL DONE!! YOU GOT IT RIGHT")

                else:
                    messages.error(request,f"INCORRECT!! The Capital of {request.POST.get('country-q')} is: {correct_answer}")        
            
            return render(request,'home.html',context={'country': random_country[0].country,'capital':random_country[0].capital_city , 'form': form, 'quiz_started': True})

    def get(self, request):
            return render(request,'home.html',{
                'quiz_started': False
            })

            
