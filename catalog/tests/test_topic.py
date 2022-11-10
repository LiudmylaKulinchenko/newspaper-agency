from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Topic

TOPICS_LIST_URL = reverse("catalog:topic-list")


class PublicTopicTests(TestCase):
    def test_login_required_list_page(self):
        resp = self.client.get(TOPICS_LIST_URL)

        self.assertNotEqual(resp.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="1test1234",
        )
        self.client.force_login(self.user)

    def test_retrieve_list_page(self):
        Topic.objects.create(name="First")
        Topic.objects.create(name="Second")

        resp = self.client.get(TOPICS_LIST_URL)

        topics = Topic.objects.all()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            list(resp.context["topic_list"]),
            list(topics),
        )
