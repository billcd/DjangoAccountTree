from enum import Enum


class PermissionType(Enum):
    READ = 0
    WRITE = 1
    DELETE = 2


def is_child_of_my_parent(me, account):
    try:
        while account.parent != me.parent:
            account = account.parent
        return True
    except AttributeError:
        return False


def check_permission(me, account, permission_type=PermissionType.READ):

    if permission_type == PermissionType.READ:
        if not is_child_of_my_parent(me, account) and me.parent != account:
            raise PermissionError("You don't have permissions to view this account.")

    elif permission_type == PermissionType.DELETE:
        if not is_child_of_my_parent(me, account) and me.parent != account:
            raise PermissionError("You don't have permissions to delete this account.")
        elif me == account:
            raise PermissionError("You can't delete yourself.")
        elif me.parent == account:
            raise PermissionError("You can't delete your parent.")

    elif permission_type == PermissionType.WRITE:
        if not is_child_of_my_parent(me, account):
            raise PermissionError("You don't have write permissions the parent account.")

    return True
