from django.test import TestCase
from accounttree.models import Account
from pprint import pprint
from accounttree.functions import slug_unique, get_account_by_slug, get_child_accounts


class AccountFunctionTest(TestCase):

    def create_account(self, account_type=Account.ORGANIZATION_TYPE, name="Test Account01", slug="test", parent=None):
        return Account.objects.create(account_type=account_type, name=name, slug=slug, parent=parent)

    def test_get_child_accounts(self):
        a = self.create_account(name='grand parent', slug=slug_unique('grand parent'))
        b = self.create_account(name='parent', slug=slug_unique('parent'), parent=a)
        self.create_account(name='child 1', slug=slug_unique('child 1'), parent=b)
        self.create_account(name='child 2', slug=slug_unique('child 2'), parent=b)

        self.assertEqual(len(get_child_accounts(b)), 2)

    def test_get_child_accounts_siblings(self):
        a = self.create_account(name='grand parent', slug=slug_unique('grand parent'))
        b = self.create_account(name='parent', slug=slug_unique('parent'), parent=a)
        self.create_account(name='uncle', slug=slug_unique('uncle'), parent=a)
        self.create_account(name='child 1', slug=slug_unique('child 1'), parent=b)
        self.create_account(name='child 2', slug=slug_unique('child 2'), parent=b)

        self.assertEqual(len(get_child_accounts(b, True)), 4)

    def test_get_account_by_slug(self):
        a = self.create_account(slug="test")
        self.assertEqual(get_account_by_slug("test"), a)

    def test_slug_unique(self):
        slug = 'test'
        a = self.create_account(slug=slug)
        self.assertNotEqual(a.slug, slug_unique(slug))

    def test_slug_unique_blank(self):
        slug = ''
        a = self.create_account(slug=slug_unique(slug))
        self.assertNotEqual(slug, a.slug)

    """
    def test_get_client_breadcrumb(self):
        test_user = self.create_account()
        account = self.create_account(slug=slug_unique('account'), parent=test_user)
        sub_account = self.create_account(slug=slug_unique('sub_account'), parent=account)

        self.assertEqual(get_client_breadcrumb(test_user, sub_account)[0], test_user)
        self.assertEqual(get_client_breadcrumb(test_user, sub_account)[1], account)
        self.assertEqual(get_client_breadcrumb(test_user, sub_account)[2], sub_account)

    def test_get_client_breadcrumb_me_is_child(self):

        account = self.create_account(slug=slug_unique('account'))
        test_user = self.create_account(parent=account)

        self.assertEqual(get_client_breadcrumb(test_user, account), [])
    """

