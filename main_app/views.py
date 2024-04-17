from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Driver
from .forms import AccoladeForm



# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars
    })
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  id_list = car.drivers.all().values_list('id')
  drivers_car_doesnt_have = Driver.objects.exclude(id__in=id_list)
  accolade_form = AccoladeForm()
  return render(request, 'cars/detail.html', { 'car': car, 'accolade_form': accolade_form, 'drivers': drivers_car_doesnt_have })

class CarCreate(CreateView):
  model = Car
  fields = ['make', 'model', 'year', 'colour', 'description']

class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars'

def add_accolade(request, car_id):
  form = AccoladeForm(request.POST)
  if form.is_valid():
    new_accolade = form.save(commit=False)
    new_accolade.car_id = car_id
    new_accolade.save()
  return redirect('detail', car_id=car_id)

class DriverList(ListView):
  model = Driver

class DriverDetail(DetailView):
  model = Driver

class DriverCreate(CreateView):
  model = Driver
  fields = '__all__'

class DriverUpdate(UpdateView):
  model = Driver
  fields = '__all__'

class DriverDelete(DeleteView):
  model = Driver
  success_url = '/drivers'

def assoc_driver(request, car_id, driver_id):
  Car.objects.get(id=car_id).drivers.add(driver_id)
  return redirect('detail', car_id=car_id)

def unassoc_driver(request, car_id, driver_id):
  Car.objects.get(id=car_id).drivers.remove(driver_id)
  return redirect('detail', car_id=car_id)