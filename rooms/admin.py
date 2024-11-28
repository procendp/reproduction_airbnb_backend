from django.contrib import admin
from .models import Room, Amenity

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = ("name", "price", "kind", "total_amenities", "owner", "created_at")
    list_filter = ("country", "city", "price", "rooms", "toilets", "pet_friendly", "kind", "amenities")

    def total_amenities(self, room):    # just test whether it is a value that will only be used in the admin panel or not when adding a new value
        return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    
    list_display = ("name", "description", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
