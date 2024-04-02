from django.urls import path
from . import views #mesma coisa de "from recipes import views"


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),

]
