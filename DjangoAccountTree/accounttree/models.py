from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    ORGANIZATION_TYPE = 'ORG'
    PERSON_TYPE = 'PER'

    ACCOUNT_TYPES = (
        (ORGANIZATION_TYPE, 'Organization'),
        (PERSON_TYPE, 'Person'),
    )

    type = models.CharField(max_length=3, choices=ACCOUNT_TYPES)
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
