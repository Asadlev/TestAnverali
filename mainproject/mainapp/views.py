from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_success')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})

def profile_success_view(request):
    return render(request, 'profile_success.html')