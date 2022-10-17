from django.urls import path

from . import views

# name from the base.html file

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'), 
# name from the base.html file
path("lines/", views.LinesView.as_view(), name='lines'), 
# name from the lines.html file
path("lines/new", views.CreateLineView.as_view(), name='create_line'), 
path("lines/<pk>/update/", views.UpdateLineView.as_view(), name='update_line'), 
path("lines/<pk>/delete/", views.DeleteLineView.as_view(), name='delete_line'), 
# name from the base.html file
path("stations/", views.StationsView.as_view(), name='stations'), 
# name from the stations.html file
path("stations/new/", views.CreateStationView.as_view(), name='create_station'), path("stations/<pk>/update/", views.UpdateStationView.as_view(), name='update_station'), path("stations/<pk>/delete/", views.DeleteStationView.as_view(), name='delete_station'), 
# name from the base.html file
path("stops/", views.StopsView.as_view(), name='stops'), 
# name from the stations.html file
path("stops/new/", views.CreateStopView.as_view(), name='create_stop'), path("stops/<pk>/update/", views.UpdateStopView.as_view(), name='update_stop'), path("stops/<pk>/delete/", views.DeleteStopView.as_view(), name='delete_stop'),
]
