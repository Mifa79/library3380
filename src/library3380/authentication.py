from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.db import connection

class SettingsBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        print(username, password, "yeah")
        with connection.cursor() as cursor:
            login_valid = cursor.execute("SELECT EXISTS(SELECT * from auth_user WHERE username= %s and password= %s)", [username, password])
            print (login_valid)

            # user = User.objects.get(username="anh")
            # print(user)

            if login_valid:
                try:
                    cursor.execute("SELECT * FROM auth_user WHERE username= %s", [username])
                    # user = dictfetchall(cursor)

                    user = User.objects.get(username=username)
                        # print(user)

                except User.DoesNotExist:
                        # Create a new user. There's no need to set a password
                        # because only the password from settings.py is checked.
                        # user = User(username=username)
                        # user.is_staff = True
                        # user.is_superuser = True
                        user = None
                return user
            return None





# def dictfetchall(cursor):
#     columns = [col[0] for col in cursor.description]
#     return [
#          dict(zip(columns, row))
#          for row in cursor.fetchall()
#     ]