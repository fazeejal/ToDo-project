# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Student
from .forms import TaskForm

class StudentListView(ListView):
    model = Student
    template_name = 'base.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = TaskForm
    template_name = 'base.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = TaskForm
    template_name = 'update.html'
    success_url = reverse_lazy('student_list')
