from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Redactor, Newspaper, Topic


def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "catalog/topic_list.html"
    paginate_by = 5
    queryset = Topic.objects.all()


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("catalog:topic-list")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5
    queryset = get_user_model().objects.all()


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = get_user_model().objects.prefetch_related("newspapers__topic")  # TODO: prefetch_related("newspapers")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdatingForm


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("catalog:redactor-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5
    queryset = Newspaper.objects.select_related("topic")  # TODO: prefetch_related("redactors")


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
