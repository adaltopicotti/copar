from django.shortcuts import render

# Create your views here.
def questionnaire2(request):
    return 'teste'

def questionnaire(request):
    return render(request, 'copar/quest1.html', {})
