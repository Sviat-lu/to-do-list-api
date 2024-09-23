import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv(override=True)


@dataclass
class APPSettings:
    """
    Database configuration settings class.

    Attributes:
        APP_HOST (str): The hostname of the application.
        APP_PORT (int): The port number on which application is running.
    """

    APP_HOST: str = os.getenv("APP_HOST", "127.0.0.1")
    APP_PORT: str = int(os.getenv("APP_PORT", 8000))


@dataclass
class DBSettings:
    """
    Database configuration settings class.

    Attributes:
        POSTGRES_HOST (str): The hostname of the PostgreSQL database.
        POSTGRES_PORT (int): The port number on which PostgreSQL is running.
        POSTGRES_DB (str): The name of the PostgreSQL database.
        POSTGRES_USER (str): The username for authenticating with the database.
        POSTGRES_PASSWORD (str): The password for authenticating with the
        database.
    """

    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT"))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")

    def __post_init__(self):
        """
        Post-initialization to ensure all required settings are provided.

        Raises:
            ValueError: If any critical database settings are missing.
        """
        if not all(
            [
                self.POSTGRES_HOST,
                self.POSTGRES_PORT,
                self.POSTGRES_DB,
                self.POSTGRES_USER,
                self.POSTGRES_PASSWORD,
            ]
        ):
            raise ValueError(
                "Some required database environment variables are missing!"
            )


@dataclass
class JWTSettings:
    """
    JWT (JSON Web Token) configuration settings class.

    Attributes:
        JWT_SECRET_KEY (str): The secret key used for signing JWT tokens.
        JWT_ACCESS_TOKEN_EXPIRES (int): The expiration time (in seconds)
        for access tokens.
    """

    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES: int = int(
        os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600)
    )

    def __post_init__(self):
        """
        Post-initialization to ensure all required settings are provided.

        Raises:
            ValueError: If the JWT secret key is missing.
        """
        if not self.JWT_SECRET_KEY:
            raise ValueError("JWT_SECRET_KEY is required!")


app_settings = APPSettings()
db_settings = DBSettings()
jwt_settings = JWTSettings()
