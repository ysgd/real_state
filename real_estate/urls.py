
from django.contrib import admin
from django.urls import path
from listings.views import list, listing_retrieve, listing_create, listing_update, listing_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list),
    path('listings/<int:pk>/',listing_retrieve),
    path('add-listing/',listing_create),
    path('edit/<int:pk>/',listing_update),
    path('listings/<pk>/delete/',listing_delete),
]
