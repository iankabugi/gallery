from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def photos(request):
    images = Image.all_images()
    return render(request, 'index.html', {"images":images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message,"images": category})
    else:
        message = "No photos under this category exist"
        return render(request, 'search.html',{"message":message})
    return render(request,"search.html")    


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html",{"image":image})
def page(request):
    return render(request,"page.html",{"title":location})
def location(request,location):
        locations = Image.filter_by_location(location)
        return render(request,'location.html',{"images": locations})