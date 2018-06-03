from django.test import TestCase
from accounttree.models import Account


class AccountTest(TestCase):

    def create_account(self, account_type=Account.ORGANIZATION_TYPE, name="Test Account01", slug="test"):
        return Account.objects.create(account_type=account_type, name=name, slug=slug)

    def test_account_creation(self):
        a = self.create_account()
        self.assertEqual(str(a), a.name)

    def test_account_creation_with_parent(self):
        a = self.create_account()
        b = self.create_account(name="Test Account 2", slug="test2")
        b.parent = a
        b.save()

        self.assertEqual(str(a) + " : " + str(b.name), str(b))
