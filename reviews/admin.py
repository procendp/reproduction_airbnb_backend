from django.contrib import admin
from .models import Review

class WordFilter(admin.SimpleListFilter):
    
    title = "Filter by words!"

    parameter_name = "p_name"

    def lookups(self, request, model_admin):
        return [("good", "Good"), ("great", "Great"), ("awesome", "Awesome")]
    
    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = ("__str__", "payload")
    list_filter = ("rating", "user__is_host", "room__category", "room__pet_friendly", WordFilter)   # customized filter with relationship