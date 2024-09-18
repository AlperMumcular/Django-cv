from django.shortcuts import render

# Create your views here.
def cv_view(request):
    return render(request, 'cv_template.html')