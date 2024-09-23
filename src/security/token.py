from datetime import timedelta
from typing import Dict

from fastapi import Response, Security
from fastapi_jwt import JwtAccessBearerCookie, JwtAuthorizationCredentials

from configs import jwt_settings

"""
An instance of JwtAccessBearerCookie used to handle JWT-based authentication
via cookies.
It is configured with a secret key and an expiration time for the access token.
"""

access_security = JwtAccessBearerCookie(
    secret_key=jwt_settings.JWT_SECRET_KEY,
    access_expires_delta=timedelta(
        minutes=jwt_settings.JWT_ACCESS_TOKEN_EXPIRES
    ),
)


async def set_token_to_cookie(response: Response) -> Dict:
    """
    Generates a new JWT access token and sets it in the response cookie.

    Args:
        response (Response): The FastAPI response object to which the token
        cookie will be added.

    Returns:
        Dict: A dictionary containing the generated access token.

    Example:
        response = Response()
        token_data = await set_token_to_cookie(response)
        print(token_data['access_token'])
    """
    subject = {"user_id": 1}
    access_token = access_security.create_access_token(subject=subject)
    access_security.set_access_cookie(response, access_token)
    return {"access_token": access_token}


async def unset_token_from_cookie(response: Response) -> None:
    """
    Unsets (removes) the JWT access token from the response cookie.

    Args:
        response (Response): The FastAPI response object from which the token
        cookie will be removed.
    """
    access_security.unset_access_cookie(response)


async def check_authorization(
    credentials: JwtAuthorizationCredentials = Security(access_security),
) -> None:
    """
    Checks the authorization of a user by validating the JWT access token from
    the request cookie.

    Args:
        credentials (JwtAuthorizationCredentials, optional): JWT credentials
        extracted from the request.
        This is automatically provided by FastAPI's dependency injection via
        Security.

    Raises:
        HTTPException: If the JWT token is invalid or expired, an exception
        will be raised.
    """
    ...
