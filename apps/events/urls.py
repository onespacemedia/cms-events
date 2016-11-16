"""URLs used by the CMS news app."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.EventListView.as_view(), name="event_list"),
    url(r"^(?P<slug>[^/]+)/$", views.EventDetailView.as_view(), name="event_detail"),
]
