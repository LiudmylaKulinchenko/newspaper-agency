from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Newspaper, Topic


NEWSPAPERS_ID = 1
NEWSPAPERS_LIST_URL = reverse("catalog:newspaper-list")
NEWSPAPERS_DETAIL_URL = reverse(
    "catalog:newspaper-detail",
    args=[NEWSPAPERS_ID]
)


class PublicNewspaperTests(TestCase):
    def test_login_required_list_page(self):
        response = self.client.get(NEWSPAPERS_LIST_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_detail_page(self):
        topic = Topic.objects.create(
            name="Test",
        )
        Newspaper.objects.create(
            id=NEWSPAPERS_ID,
            title="Test title",
            topic=topic,
        )

        response = self.client.get(NEWSPAPERS_DETAIL_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )

        self.client.force_login(self.user)

    def test_retrieve_list_page(self):
        topic = Topic.objects.create(
            name="Test",
        )
        Newspaper.objects.create(
            title="Frist test title",
            topic=topic,
        )
        Newspaper.objects.create(
            title="Second test title",
            topic=topic,
        )

        response = self.client.get(NEWSPAPERS_LIST_URL)
        newspapers = Newspaper.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspapers),
        )

    def test_retrieve_detail_page(self):
        topic = Topic.objects.create(
            name="Test",
        )
        Newspaper.objects.create(
            id=NEWSPAPERS_ID,
            title="Frist test title",
            topic=topic,
        )

        response = self.client.get(NEWSPAPERS_DETAIL_URL)

        self.assertEqual(response.status_code, 200)
