from django.shortcuts import render, get_object_or_404, redirect
from .models import EmpresarialQuest
from .forms import EmpresarialQuestForm
# Create your views here.
def questionnaire2(request):
    return 'teste'

def questionnaire(request):

    if request.method == "POST":
        form = EmpresarialQuestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "copar/empresarial.html", {"form": form})

    return render(request, 'copar/empresarial.html', {"form": EmpresarialQuestForm})


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
