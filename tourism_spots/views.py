from django.shortcuts import render
from django.http import JsonResponse
from .models import TouristSpot
from django.http import JsonResponse
from .models import TouristSpot



def home(request):
    # Renders the main map page using the base template
    return render(request, 'home.html')



def tourist_spots_data(request):
    spots = TouristSpot.objects.all()
    data = []
    for spot in spots:
        data.append({
            "name": spot.name,
            "barangay": spot.barangay,
            "lat": spot.latitude,
            "lng": spot.longitude,
            "description": spot.description,
            "images": [img.image.url for img in spot.images.all()]
        })
    return JsonResponse(data, safe=False)



