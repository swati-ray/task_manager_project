from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission: owners can edit/delete their tasks; admin can do anything.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any authenticated user
        if request.method in SAFE_METHODS:
            return True
        # Admin can edit/delete any task
        if request.user.is_staff:
            return True
        # Otherwise only owner can edit/delete
        return obj.owner == request.user
