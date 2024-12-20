from django.urls import path
from .views import PerkDetail, Perks, Experiences, ExperienceDetail, ExperiencePerks, ExperienceBookings, ExperienceBookingDetail

urlpatterns = [
    path("", Experiences.as_view()),
    path("<int:pk>", ExperienceDetail.as_view()),
    path("<int:pk>/perks", ExperiencePerks.as_view()),
    path("<int:pk>/bookings", ExperienceBookings.as_view()),
    path("<int:pk>/bookings/<int:booking_pk>", ExperienceBookingDetail.as_view()),
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetail.as_view())
]