from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import EmpresarialQuest
from .forms import EmpresarialQuestForm
# Create your views here.
def home(request):
    return render(request, "copar/home.html", {"date":timezone.now()})

def emp_questionnaire(request):

    if request.method == "POST":
        form = EmpresarialQuestForm(request.POST)
        if form.is_valid():
            last_reg = EmpresarialQuest.objects.last()
            new = form.save(commit=False)
            new.id = last_reg.id + 1
            new.insert_date = timezone.now()
            new.save()
            return render(request, "copar/home.html", {"date":timezone.now()}) # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "copar/quest_emp.html", {"form": form})
    return render(request, 'copar/quest_emp.html', {"form": EmpresarialQuestForm})

def emp_list(request):
    quest = EmpresarialQuest.objects.filter(insert_date__lte=timezone.now()).order_by('-insert_date')
    recent_quest = EmpresarialQuest.objects.filter(insert_date__lte=timezone.now()).order_by('-insert_date')[:3]
    return render(request, 'copar/list_emp.html', {'quests': quest, 'recent_quests': recent_quest})

def new_edit(request, pk):
    new = get_object_or_404(New, pk=pk)
    if request.method == "POST":
        form = NewForm(request.POST, instance=new)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.published_date = timezone.now()
            new.save()
            return redirect('new_detail', pk=new.pk)
    else:
        form = NewForm(instance=new)
    return render(request, 'cotador/new_edit.html', {'form': form})
