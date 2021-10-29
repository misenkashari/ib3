from django.contrib import admin
from django.urls import path, include
from questions.views import landing_page

urlpatterns = [
    path('', landing_page, name="landing"),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('questions/', include('questions.urls', namespace='questions')),
]
