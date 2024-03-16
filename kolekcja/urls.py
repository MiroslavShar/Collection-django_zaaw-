"""
URL configuration for Collection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from kolekcja import views

urlpatterns = [
    path('cos/', views.CosTamView.as_view(), name='cos'),
    path('add_type/', views.Add_type.as_view(), name='type'),
    path('add_coin/', views.Add_coin.as_view(), name='coin'),
    path('add_metal/', views.Add_metal.as_view(), name='metal'),
    path('show_metal/', views.Show_metal.as_view(), name='show_metal'),
    path('show_metal/<int:id>', views.UpdateMetalView.as_view(), name='metal_id'),
    path('show_type/', views.Show_types.as_view(), name='show_types'),
    path('add_category/', views.Add_category.as_view(), name='add_category'),
    path('add_category_form/', views.AddCategoryForm.as_view(), name='add_category_form'),
    path('show_coins/', views.Show_coin.as_view(), name='show_coins'),
    path('show_coins/<int:id>/', views.UpdateCoinView.as_view(), name='coins_id'),
    path('add_coin_to_collection/<int:coin_id>/', views.AddToCollectionCoint.as_view(), name='add_coin_to_collection'),
    path('collection/', views.MyCollectionview.as_view(), name='collection'),


]
