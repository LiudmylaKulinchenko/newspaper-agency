from django.urls import path

from catalog.views import (
    index,
    TopicListView,
    RedactorListView,
    NewspaperListView,
    RedactorDetailView,
    NewspaperDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create",
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
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
