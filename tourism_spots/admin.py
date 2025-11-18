from django.contrib import admin
from .models import TouristSpot
from django.contrib import admin
from .models import TouristSpot, TouristSpotImage


class TouristSpotImageInline(admin.TabularInline):
    model = TouristSpotImage
    extra = 1  # Show 1 empty image field by default


class TouristSpotAdmin(admin.ModelAdmin):
    inlines = [TouristSpotImageInline]


admin.site.register(TouristSpot, TouristSpotAdmin)
admin.site.register(TouristSpotImage)