from django.shortcuts import render
from .forms import JobApplicationForm

def home(request):
    return render(request, 'home.html')

def job_apply(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = JobApplicationForm()

    return render(request, 'job_form.html', {'form': form})