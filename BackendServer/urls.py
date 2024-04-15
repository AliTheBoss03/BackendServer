# backend/urls.py
from django.urls import path
from backend.views import gem_bruger

urlpatterns = [
    path('gem-bruger/', gem_bruger, name='gem_bruger'),
]

def home(request):
    return HttpResponse('Hello, Django!')
    urlpatterns = [
    path('', home, name='home'),
    path('gem-bruger/', gem_bruger, name='gem_bruger'),
]
