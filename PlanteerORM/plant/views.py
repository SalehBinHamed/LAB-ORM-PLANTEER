from django.shortcuts import render , redirect ,get_object_or_404
from .models import Plant
from django.core.paginator import Paginator
# Create your views here.

def home_views(request):
    categories = Plant.CategoryChoices.choices
    featured_plants = Plant.objects.order_by('-created_at')[:3]
    return render(request, 'main/index.html', {'categories': categories, 'featured_plants': featured_plants})


def create_views(request):
    if request.method == "POST":
        new_plant = Plant(
            name=request.POST.get("name"),
            about=request.POST.get("about"),
            used_for=request.POST.get("used_for"),
            category=request.POST.get("category", ""),
            image=request.FILES.get("image"),
            is_edible=request.POST.get("is_edible") == "on",
        )
        new_plant.save()
        return redirect('plant:home') 
    return render(request, 'main/create.html',{"CategoryChoices": Plant.CategoryChoices.choices})

def all_views(request):
    plant_list = Plant.objects.all().order_by('id')
    paginator = Paginator(plant_list, 8)  

    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/all.html', {'page_obj': page_obj})


def details_views(request , plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    other_plants = Plant.objects.filter(category=plant.category).exclude(id=plant_id)[:3]
    return render(request, 'main/prodectdtails.html', {"plant": plant, "other_plants": other_plants})

def delete_views(request, plant_id):
    if request.method == "POST":
        plant = get_object_or_404(Plant, id=plant_id)
        plant.delete()
        return redirect('plant:all_views') 


def update_views(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST.get("about")
        plant.used_for = request.POST.get("used_for")
        plant.category = request.POST.get("category", "")
        plant.image = request.FILES.get("image", plant.image) 
        plant.is_edible = request.POST.get("is_edible", False) == 'on'
        plant.save()
        return redirect('plant:details_views', plant_id=plant.id)  

    else:
        CategoryChoices = Plant.CategoryChoices.choices
    return render(request, 'main/update.html', {'plant': plant, 'CategoryChoices': CategoryChoices})



def search_views(request):
    plants = Plant.objects.all()

    search_term = request.GET.get('search', '')
    if len(search_term) >= 3:
        plants = plants.filter(name__icontains=search_term)

    category = request.GET.get('category', '')
    if category:
        plants = plants.filter(category=category)

    is_edible = request.GET.get('is_edible')
    if is_edible == 'on':
        plants = plants.filter(is_edible=True)

    if 'order_by' in request.GET:
        order_by = request.GET['order_by']
        if order_by == 'category':
            plants = plants.order_by('category')
        elif order_by == 'created_at':
            plants = plants.order_by('-created_at')

    categories = Plant.CategoryChoices.choices

    return render(request, 'main/search.html', {"plants": plants, "categories": categories})
