from django.forms import ModelForm
from .models import Account


class AccountFormBasicOrg(ModelForm):
    class Meta:
        model = Account
        exclude = ('user', )
