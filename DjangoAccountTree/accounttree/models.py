from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    ORGANIZATION_TYPE = 'ORG'
    PERSON_TYPE = 'PER'

    ACCOUNT_TYPES = (
        (ORGANIZATION_TYPE, 'Organization'),
        (PERSON_TYPE, 'Person'),
    )

    GLOBAL_ADMIN_LEVEL = 'GAL'
    CLIENT_OWNER_LEVEL = 'COL'
    CLIENT_ADMIN_LEVEL = 'CAL'
    CLIENT_USER_LEVEL = 'CUL'
    CLIENT_CONTACT_LEVEL = 'CCL'

    ACCOUNT_LEVELS = (
        (GLOBAL_ADMIN_LEVEL, 'Global Admin'),
        (CLIENT_OWNER_LEVEL, 'Account Owner'),
        (CLIENT_ADMIN_LEVEL, 'Administrator'),
        (CLIENT_USER_LEVEL, 'User'),
        (CLIENT_CONTACT_LEVEL, 'Contact'),
    )

    type = models.CharField(max_length=3, choices=ACCOUNT_TYPES)
    account_level = models.CharField(max_length=3, choices=ACCOUNT_LEVELS)
    name = models.CharField(max_length=50)
    _updated = models.DateTimeField(auto_now=True)
    _created = models.DateTimeField(auto_now=False, auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="account_owner", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="account", null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        if self.parent and self != self.parent:
            return self.parent.name + " - " + self.name
        else:
            return self.name
