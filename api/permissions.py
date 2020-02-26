from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    message = "You must be the author of this article."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.added_by == request.user):
            return True
        else:
            return False
