from rest_framework.authentication import TokenAuthentication


class BearerTokenAuthentication(TokenAuthentication):
    """Accept 'Authorization: Bearer <token>' (Insomnia's Bearer option) as well as 'Token <token>'."""
    keyword = 'Bearer'
