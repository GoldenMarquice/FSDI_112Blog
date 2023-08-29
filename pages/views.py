from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class DeletePageView(TemplateView):
    template_name = "pages/delete.html"

class EditPageView(TemplateView):
    template_name = "pages/edit.html"

class BonusStagePageView(TemplateView):
    template_name = "pages/bonus.html"
    
def slideshow_view(request):
    slideshow_images = [
        'path/to/bison.jpeg',
        'path/to/blanka.jpg',
        'path/to/Chun-Li.jpg',
        'path/to/Ryu.jpg',
        'path/to/Sonya.jpg',
        'path/to/Vega.jpg',
        # Add more image paths here
    ]
    return render(request, 'slideshow.html', {'slideshow_images': slideshow_images})