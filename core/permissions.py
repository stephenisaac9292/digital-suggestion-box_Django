from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("Submitted by:", obj.submitted_by.id)
        print("Current user:", request.user.id)
        
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_staff or request.user.is_superuser:
            return True

        return obj.submitted_by == request.user

