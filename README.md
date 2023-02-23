# API of project "Yatube".

## Description

The API is fully accessible only to authenticated users (JWT-tokens + Djoser).

Authenticated user has the right to change and delete their content; otherwise, read-only access.

Unauthenticated users have read-only access to the API.
The exception is the /follow/ endpoint: access to it is granted only to authenticated users.

Adding new users via the API is not possible.

Full API documentation is available at endpoint:
>redoc/

## Examples of requests

- getting JWT-token *(POST)*
>api/v1/jwt/create/ 
>```json
>{
>    "username": "my_username",
>    "password": "my_password"
>}
>```

- refreshing JWT-token *(POST)*
>api/v1/jwt/refresh/ 
>```json
>{
>    "refresh": "refresh token"
>}
>```

- verifying JWT-token *POST)*
>api/v1/jwt/verify/ 
>```json
>{
>    "token": "refresh or access token"
>}
>```

## Technology

Python 3.7

Django 2.2.16

Django REST framework 3.12.4

Simple JWT 4.7.2

## For launch

Create and activate virtual environment
```
py -3.7 -m venv venv

source venv/Scripts/activate
```

Install dependencies from requirements.txt file
```
pip install -r requirements.txt
```

Perform migrations
```
py manage.py migrate
```

Run project
```
py manage.py runserver 8008
```

## Author

[NotMainCode](https://github.com/NotMainCode)
