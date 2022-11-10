from django.urls import path

from catalog.views import (
    index,
    TopicListView,
    RedactorListView,
    NewspaperListView,
    RedacteorDetailView,
    NewspaperDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path(
        "redactors/<int:pk>/",
        RedacteorDetailView.as_view(), name="redactor-detail"
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(), name="newspaper-detail"
    ),
]

app_name = "catalog"
