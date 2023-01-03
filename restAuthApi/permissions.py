from rest_framework.permissions import BasePermission


class MyCustomPermission(BasePermission):
    def has_permission(self, request, view):
        # register user can read and write api
        if request.method == 'POST' or request.method == 'GET':
            return True

        return False