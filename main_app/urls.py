from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('markers/', views.marker_index, name='marker-index'),
    path('markers/<int:marker_id>/', views.marker_detail, name='marker-detail'),
    path('markers/create/', views.MarkerCreate.as_view(), name='marker-create')
    # path('update/', views.update, name='update'),
    # path('delete/', views.delete, name='delete'),
]
