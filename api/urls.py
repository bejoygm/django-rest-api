from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls
from .views import CreateView, DetailsView

urlpatterns = {
    path('team/', CreateView.as_view(), name="create"),
    path('team/<user_id>/', DetailsView.as_view(), name="details"),
    path('docs/', include_docs_urls(title='Manage Team APIs'))
}

urlpatterns = format_suffix_patterns(urlpatterns)