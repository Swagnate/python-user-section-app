# sections/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Section
from .forms import UserForm, SectionForm

def index(request):
    return render(request, 'sections/index.html')

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'sections/section_list.html', {'sections': sections})

def user_list(request):
    users = User.objects.all()
    return render(request, 'sections/user_list.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Устанавливаем пароль
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'sections/create_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'sections/delete_user.html', {'user': user})

def create_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'sections/create_section.html', {'form': form})

def delete_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    if request.method == 'POST':
        section.delete()
        return redirect('section_list')
    return render(request, 'sections/delete_section.html', {'section': section})

def remove_user_from_section(request, section_id, user_id):
    section = get_object_or_404(Section, id=section_id)
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        section.users.remove(user)  # Удаляем пользователя из секции
        return redirect('section_list')
    return render(request, 'sections/remove_user_from_section.html', {'section': section, 'user': user})

