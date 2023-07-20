from django.urls import path
from . import views

# We are adding a URL called /dashboard & about
urlpatterns = [
    path(''      , views.dashboard_DEF, name='dashboard-URL'),
    # path('about' , views.about, name='about-URL'),
]
