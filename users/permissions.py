from rest_framework.permissions import BasePermission

from users.models import UserRoles, User

user = User()


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


