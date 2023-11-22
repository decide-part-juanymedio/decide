from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import get_object_or_404
from base import mods
from django.contrib.auth.models import User

UserModel = get_user_model()

class AuthBackend(ModelBackend):
    '''
    This class makes the login to the authentication method for the django
    admin web interface.

    If the content-type is x-www-form-urlencoded, a requests is done to the
    authentication method to get the user token and this token is stored
    for future admin queries.
    '''

    def authenticateUsernameOrEmail(self, request, username=None, password=None, **kwargs):
        """
        Esta función segun los datos que se introduzcan en el formulario de login 
        accederá al usuario bien por su username o bien por su email.

        :param username: puede ser el username o el email del usuario
        :type username: str
        :param password: la password del usuario
        :type password: str
        :return: el user que corresponda al username o el email dado
        :rtype: User
        """

        if username is None:
            if '@' in username:
                username = kwargs.get(UserModel.EMAIL_FIELD)
            else:
                username = kwargs.get(UserModel.USERNAME_FIELD)

        if username is None or password is None:
            return
        try:
            if '@' in username:
                user = get_object_or_404(User, email=username)
            else:
                user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            
            UserModel().set_password(password)
        else:
            if user.check_password(password)and self.user_can_authenticate(user):
                return user
            

    def authenticate(self, request, username=None, password=None, **kwargs):
        #u = super().authenticate(request, username=username,
          #                       password=password, **kwargs)
        u=self.authenticateUsernameOrEmail(request, username=username, password=password, **kwargs)
        # only doing this for the admin web interface
        if u and request.content_type == 'application/x-www-form-urlencoded':
            data = {
                'username': username,
                'password': password,
            }
            token = mods.post('authentication', entry_point='/login/', json=data)
            request.session['auth-token'] = token['token']

        return u
