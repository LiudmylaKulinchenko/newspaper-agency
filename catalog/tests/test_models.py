from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Topic, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="Test",
        )

        self.assertEqual(
            str(topic),
            topic.name
        )

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="Test first",
            last_name="Test last",
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name="Test",
        )
        newspaper = Newspaper.objects.create(
            title="Test model",
            content="Test content",
            topic=topic,
        )

        date = newspaper.published_date.strftime("%d/%m/%Y")

        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} (topic: {newspaper.topic}, date: {date})"
        )

    def test_create_redactor_with_years_of_expirience(self):
        username = "test"
        password = "1test1234"
        years_of_expirience = 5

        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_expirience=years_of_expirience,
        )

        self.assertEqual(redactor.username, username)
        self.assertTrue(redactor.check_password, password)
        self.assertEqual(redactor.years_of_expirience, years_of_expirience)
