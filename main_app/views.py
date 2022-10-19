from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Package

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def package_index(request):
    packages = Package.objects.all()
    return render(request, 'packages/index.html', {'packages': packages})

def package_detail(request, package_id):
    package = Package.objects.get(id=package_id)
    return render(request, 'packages/detail.html', {
        'package': package
        })

def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Signup Input Invalid - Please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class PackageCreate(CreateView):
    model = Package
    fields = ('name', 'description')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PackageUpdate(UpdateView):
    model = Package
    fields = '__all__'

class PackageDelete(DeleteView):
    model = Package
    success_url = '/packages/'