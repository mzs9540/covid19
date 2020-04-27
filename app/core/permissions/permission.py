from rest_framework import permissions


class PermissionsForStaff(permissions.BasePermission):
    """Define permission for News ViewSet Methods"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user and \
                   request.user.is_authenticated \
                   and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return request.user and \
            request.user.is_authenticated and request.user.is_staff
