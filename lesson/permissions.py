from rest_framework.permissions import BasePermission

from users.models import UserRoles, User

user = User()


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsNotModerator(BasePermission):
    def has_permission(self, request, view):
        return not user.groups.filter(name='Moderator')