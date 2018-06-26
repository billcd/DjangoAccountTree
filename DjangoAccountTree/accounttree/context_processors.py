from .models import Account
from .functions import get_child_accounts


def account_processor(request):
    try:
        me = Account.objects.get(user=request.user)
        return {'me': me, 'child_accounts': get_child_accounts(me)}
    except (TypeError, Account.DoesNotExist):
        return {'me': None, 'child_accounts': None}

