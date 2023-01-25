from django.shortcuts import render

# Create your views here.

def adminDashboard(request):
    return render(request, 'untangledStringsAdmin/adminDashboard.html')
