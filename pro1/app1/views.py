from django.shortcuts import render, redirect
from .models import Voters
from .forms import VotersForm

# Create your views here.
def homeview(request):
    return render(request, 'app1/home.html', {})

def formview(request):
    form = VotersForm()
    if request.method == 'POST':
        form = VotersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def showview(request):
    obj = Voters.objects.all()
    return render(request, 'app1/show.html', {'obj': obj})

def showDetailsview(request,pk):
    obj = Voters.objects.get(vid=pk)
    return render(request, 'app1/details.html',{'obj': obj})

def updateview(request, x):
    obj = Voters.objects.get(vid=x)
    form = VotersForm(instance=obj)
    if request.method == 'POST':
        form = VotersForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/a1/sdv/{obj.vid}/')
    return render(request, 'app1/form.html', {'form': form})

def deleteview(request, y):
    obj = Voters.objects.get(vid=y)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/success.html', {'obj': obj})

def errorview(request, exception):
    return render(request, 'app1/ErrorPagee.html', {}, status=404)