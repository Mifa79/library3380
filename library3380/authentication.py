from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import connection

User = get_user_model()

class SettingsBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        
        with connection.cursor() as cursor:
            login_valid = cursor.execute("SELECT EXISTS(SELECT * from sign_up_user WHERE username= %s and password= %s)", [username, password])
            if login_valid:
                try:
                    cursor.execute("SELECT * FROM sign_up_user WHERE username= %s", [username])
                    user = User.objects.get(username=username)

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