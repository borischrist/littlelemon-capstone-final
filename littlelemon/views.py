from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect(reverse('restaurant:home')+"?msg=SIGNUPOK")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'page_title':'Sign up', 'form': form})
  