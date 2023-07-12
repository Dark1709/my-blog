from django.urls import path
from .views import hi_publication
""" from apps.publication.views import hi_publication """
""" from apps.publication import views """


urlpatterns = [
    path('publication', hi_publication ),
]