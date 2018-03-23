from django.urls import path

from django.views.generic import TemplateView
from . import views
# Create your views here.


app_name = 'seo'


urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="project_robots_file"),
]