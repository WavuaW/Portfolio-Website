from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# generate a token for user login

def generate_auth_token(user:User):
    """
        description - generate tokens for user
    """

    refresh = RefreshToken.for_user(user)

    tokens = {
        "access_token": str(refresh.access_token),
        "refresh": str(refresh),
    }

    return tokens