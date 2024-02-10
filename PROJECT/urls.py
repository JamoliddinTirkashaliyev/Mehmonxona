from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('buyurtma/', buyurtma),
    path('buyurtma_ochir/<int:pk>/', buyurtma_ochir),
    path('buyurtma/<int:pk>/tahrirlash/', buyurtma_tahrirlash),
    path('lavozim/', lavozim),
    path('lavozim_ochir/<int:pk>/', lavozim_ochir),
    path('lavozim/<int:pk>/tahrirlash/', lavozim_tahrirlash),
    path('xodim/', xodim),
    path('xodim/<int:pk>/tahrirlash/', xodim_tahrirlash),
    path('xodim_ochir/<int:pk>/', xodim_ochir),
    path('xona/', xona),
    path('xona_ochir/<int:pk>/', xona_ochir),
    path('xona/<int:pk>/tahrirlash/', xona_tahrirlash),

]
