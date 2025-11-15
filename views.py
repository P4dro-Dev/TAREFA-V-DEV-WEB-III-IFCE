from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor
from .forms import AutorForm
from django.db.models import Q

def index(request):
    return redirect('autor_list')

def autor_list(request):
    q = request.GET.get('q','')
    if q:
        autores = Autor.objects.filter(Q(nome__icontains=q) | Q(email__icontains=q)).order_by('-criado_em')
    else:
        autores = Autor.objects.all().order_by('-criado_em')
    return render(request,'autor_list.html',{'autores':autores,'q':q})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request,'autor_form.html',{'form':form,'action':'Criar'})

def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request,'autor_form.html',{'form':form,'action':'Alterar'})

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    return render(request,'autor_confirm_delete.html',{'autor':autor})

def autor_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request,'autor_detail.html',{'autor':autor})
