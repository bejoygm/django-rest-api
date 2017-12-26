from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    path('team/', CreateView.as_view(), name="create"),
    path('team/<user_id>/', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)