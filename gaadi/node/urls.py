from django.contrib import admin
from django.urls import path
from django.views import View
from .views import controlCommandView

urlpatterns = [
    #path('admin/', admin.site.urls),
     path('test/',controlCommandView.as_view()),
]
