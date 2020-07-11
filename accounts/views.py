from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from accounts.forms import UserCreationForm


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
    return render(request, 'register.html', {'form': form})