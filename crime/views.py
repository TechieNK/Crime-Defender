from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name != '':
            return render(request,'crime/front.html')
    return render(request, 'crime/front.html')
