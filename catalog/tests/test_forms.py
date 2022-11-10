from django.test import TestCase

from catalog.forms import RedactorCreationForm


class FormsTests(TestCase):
    def test_redactor_creation_with_first_last_name_license_number_valid(self):
        form_data = {
            "username": "test",
            "password1": "1test1234",
            "password2": "1test1234",
            "email": "test@test.com",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_expirience": 5,
        }

        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
