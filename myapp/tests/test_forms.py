from django.test import SimpleTestCase
from myapp.forms import GenerateUserForm
class TestForms(SimpleTestCase):

    def test_generateuserform_is_valid(self):
        form = GenerateUserForm(data={
            'total_user_input':20
        })
        #valid if it is integer >= 10
        self.assertTrue(form.is_valid())

    def test_generateuserform_is_integer_not_valid(self):
        form = GenerateUserForm(data={
            'total_user_input':5
        })
        #valid if it is integer >= 10
        self.assertFalse(form.is_valid())        

    def test_generateuserform_is_string_not_valid(self):
        form = GenerateUserForm(data={
            'total_user_input':'abc'
        })
        #valid if it is integer >= 10
        self.assertFalse(form.is_valid())                