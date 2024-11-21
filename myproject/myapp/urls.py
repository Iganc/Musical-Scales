from django.urls import path

from . import views
from .views import home, process_note, test_template, explore_scales_view

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('process/', views.process_note, name='process_note'),  # Process note form submission
    path('explore-scales/', views.explore_scales_view, name='explore-scales'),
    path('explore-chords/', views.explore_chords, name='explore-chords'),  # Explore chords page
    path('identify-chords/', views.identify_chords, name='identify-chords'),
    path('identify-scales/', views.identify_scales, name='identify-scales'),
    path('test/', test_template, name='test-template'),
]

