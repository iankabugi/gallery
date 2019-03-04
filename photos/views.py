from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def photos(request):
    images = Image.all_images()
    return render(request, 'gallery.html', {"images":images})


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search_image.html',{"message":message,"images": searched_images})
    else:
        message = "No photos under this category exist"
        return render(request, 'search_image.html',{"message":message})
    return render(request,"search_image.html")    


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html",{"image":image})
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')