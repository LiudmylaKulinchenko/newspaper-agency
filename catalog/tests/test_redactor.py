from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

REDACTORS_ID = 1
REDACTORS_LIST_URL = reverse("catalog:redactor-list")
REDACTORS_DETAIL_URL = reverse("catalog:redactor-detail", args=[REDACTORS_ID])


class PublicRedactorTests(TestCase):
    def test_login_required(self):
        response = self.client.get(REDACTORS_LIST_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_detail_page(self):
        get_user_model().objects.create_user(
            id=REDACTORS_ID,
            username="test",
            password="test1234",
        )

        response = self.client.get(REDACTORS_DETAIL_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.client.force_login(self.user)

    def test_retrieve_list_page(self):
        get_user_model().objects.create_user(
            username="First redactor",
            password="first1234",
        )
        get_user_model().objects.create_user(
            username="Second redactor",
            password="second1234",
            years_of_expirience=3,
        )

        response = self.client.get(REDACTORS_LIST_URL)

        redactors = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactors),
        )

    def test_retrieve_detail_page(self):
        user_id = self.user.id

        response = self.client.get(reverse(
            "catalog:redactor-detail",
            args=[user_id])
        )

        self.assertEqual(response.status_code, 200)
