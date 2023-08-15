from django . urls import path
from . import views

urlpatterns = [
    path('food_card/',views.food_card)
]
 