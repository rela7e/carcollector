from django.shortcuts import render

cars = [
    {'make': 'Chevrolet', 'model': 'Camaro', 'year': '1972', 'colour': 'red'},
    {'make': 'Ford', 'model': 'Mustang', 'year': '1970', 'colour': 'black'},
]



# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def cars_index(request):
    return render(request, 'cars/index.html', {
        'cars': cars
    })