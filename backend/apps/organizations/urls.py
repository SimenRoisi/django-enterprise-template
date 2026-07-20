from django.urls import path

from apps.organizations import views

urlpatterns = [
    path(
        "organizations/",
        views.OrganizationListView.as_view(),
        name="list-organizations",
    ),
]