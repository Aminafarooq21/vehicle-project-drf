from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:

            return request.user.is_authenticated

        return request.user.is_authenticated and hasattr(request.user, 'owner')

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:

            return True

        return request.user.is_authenticated and obj.user == request.user.Owner
