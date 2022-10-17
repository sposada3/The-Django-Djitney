from django.shortcuts import render
from .models import Line, Station, Stop
from .forms import  StopForm, LineForm, StationForm
# Add your imports below:
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class HomeView(TemplateView):
  template_name = "routes/home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["lines"] = Line.objects.all()
    context["stations"] = Station.objects.all()
    context["stops"] = Stop.objects.all()
    return context

# Create your views here.
# List view
class LinesView(ListView):
  template_name = "routes/lines.html"
  model = Line

# Create view
class CreateLineView(CreateView):
  template_name = "routes/add_line.html"
  model = Line
  form_class = LineForm

# Update view
class UpdateLineView(UpdateView):
  template_name = "routes/update_line.html"
  model = Line
  form_class = LineForm

# Delete view
class DeleteLineView(DeleteView):
  template_name = "routes/delete_line.html"
  model = Line
  success_url = "/lines"

# List view
class StationsView(ListView):
  template_name = "routes/stations.html"
  model = Station

# Create view
class CreateStationView(CreateView):
  template_name = "routes/add_station.html"
  model = Station
  form_class = StationForm

# Update view
class UpdateStationView(UpdateView):
  template_name = "routes/update_station.html"
  model = Station
  form_class = StationForm

# Delete view
class DeleteStationView(DeleteView):
  template_name = "routes/delete_station.html"
  model = Station
  success_url = "/stations/"

# List view
class StopsView(ListView):
  template_name = "routes/stops.html"
  model = Stop

# Create view
class CreateStopView(CreateView):
  template_name = "routes/add_stop.html"
  model = Stop
  form_class = StopForm

# Update view
class UpdateStopView(UpdateView):
  template_name = "routes/update_stop.html"
  model = Stop
  form_class = StopForm

# Delete view
class DeleteStopView(DeleteView):
  template_name = "routes/delete_stop.html"
  model = Stop
  success_url = "/stops/"
