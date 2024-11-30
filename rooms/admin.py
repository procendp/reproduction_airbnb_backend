from django.contrib import admin
from .models import Room, Amenity

# Register your models here.

@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices, )
    
    list_display = ("name", "price", "kind", "total_amenities", "rating", "owner", "created_at")
    list_filter = ("country", "city", "price", "rooms", "toilets", "pet_friendly", "kind", "amenities")
    search_fields = ("name", "price")   # ^name : startswith, =name : 동일한 값만 취급

    # def total_amenities(self, room):    # just test whether it is a value that will only be used in the admin panel or not when adding a new value
    #     return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    
    list_display = ("name", "description", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
