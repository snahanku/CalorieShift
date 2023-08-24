from django.shortcuts import render
from django.http import HttpResponse

def display_name(request):
    return render(request, 'home.html')

# Create your views here.

from django.shortcuts import render
from django.template import loader
import json
import requests
#api_key=LQeKfQgZZC9C9ei04qpYvg==MJYJQ5xl14opYcrD
#API_URL=https://api.api-ninjas.com/v1/nutrition?query=
posted_value=0
# Create your views here.
def home(request):
    #template =loader.get_template("home.html")

    context ={
        "message":"hello",
        "data" : [1,2,3,4,5]
    }
    #import json
    #import requests

    if request.method == 'POST':
        query= request.POST['query']
        posted_value= query
        api_url= 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request= requests.get(api_url+ query, headers={'X-Api-Key': 'LQeKfQgZZC9C9ei04qpYvg==MJYJQ5xl14opYcrD'})
        api= json.loads( api_request.content)
        try:
             api= json.loads( api_request.content)
             print( api_request.content)
        except Exception as e:
            api ="error "
            print(e)
        print("its working")
        AvgBurnRate=4.5
        value= api[0]["calories"]
        time=int(value/AvgBurnRate)

        caloriesBurnedPerMinute = 10
        joggingTime =int( value / caloriesBurnedPerMinute)

        caloriesBurnedPerMinute = 5
        briskWalkingTime = int(value / caloriesBurnedPerMinute)

        caloriesBurnedWeight=4.7
        weightLiftingTime =int(value/ caloriesBurnedWeight)





        return render(request , "home.html",{'api':api , "time":time , "joggingTime": joggingTime , "briskWalkingTime": briskWalkingTime , "weightLiftingTime":weightLiftingTime})
    else:
        return render(request , "home.html",context)



def calorie_Yoga_meter(request):
    api_url= 'https://api.api-ninjas.com/v1/nutrition?query='
    api_request= requests.get(api_url,  headers={'X-Api-Key': 'LQeKfQgZZC9C9ei04qpYvg==MJYJQ5xl14opYcrD'})
    api= json.loads(api_request.content)
   #averageBurnRatePerMinute = 4.8 
   #timeInMinutes = calories / averageBurnRatePerMinute
    value=5
    return render(request , "new.html" , {'cal':posted_value})
