from fastapi import APIRouter, Response, status

from security import set_token_to_cookie, unset_token_from_cookie

router = APIRouter()


@router.get(
    path="/login/",
    status_code=status.HTTP_200_OK,
    summary="User login",
    description=(
        "Handles user login by setting an authentication token in the "
        "response cookies. This token is used for subsequent authenticated "
        "requests."
    ),
)
async def login(response: Response) -> Response:
    """
    Handle user login by setting the authentication token in the cookies.

    This endpoint generates an authentication token and stores it in the
    response cookies to allow the user to make authenticated requests
    in the future.

    Args:
        response (Response): The response object where the token will be set.

    Returns:
        Response: The response with the token stored in cookies.
    """
    return await set_token_to_cookie(response)


@router.get(
    path="/logout/",
    status_code=status.HTTP_200_OK,
    summary="User logout",
    description=(
        "Handles user logout by removing the authentication token from the "
        "response cookies. "
        "This action revokes the user's authentication."
    ),
)
async def logout(response: Response) -> None:
    """
    Handle user logout by removing the authentication token from the cookies.

    This endpoint revokes the user's authentication by removing the token
    stored in the cookies.

    Args:
        response (Response): The response object where the token will be
        removed.

    Returns:
        None: The token is removed from the cookies.
    """
    await unset_token_from_cookie(response)
