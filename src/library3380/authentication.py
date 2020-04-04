from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.db import connection

class SettingsBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        with connection.cursor() as cursor:
            login_valid = cursor.execute("SELECT EXISTS(SELECT * from auth_user WHERE username= %s and password= %s)", [username, password])
            if login_valid:
                try:
                    cursor.execute("SELECT * FROM auth_user WHERE username= %s", [username])
                    user = User.objects.get(username=username)
                    print("this is user object", user)

                except User.DoesNotExist:
                        # Create a new user. There's no need to set a password
                        # because only the password from settings.py is checked.
                        # user = User(username=username)
                        # user.is_staff = True
                        # user.is_superuser = True
                        user = None
                return user
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None