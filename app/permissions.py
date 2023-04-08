from rest_framework import permissions


class ReaderAccessPermission(permissions.BasePermission):
    message = 'You can only work with your Reader'

    def has_object_permission(self, request, view, obj):
        if request.is_authenticated or request.user.is_staff:
            return True
        return False
