# API of project "Yatube".

## Description

The API is fully accessible only to authenticated users (JWT-tokens + Djoser).

Authenticated user has the right to change and delete their content; otherwise, read-only access.

Unauthenticated users have read-only access to the API.
The exception is the /follow/ endpoint: access to it is granted only to authenticated users.

Adding new users via the API is not possible.

Full API documentation is available at endpoint:
>redoc/

## Endpoints

- getting JWT-token *(POST)*
>api/v1/jwt/create/ 
>```
>{
>    "username": "my_username",
>    "password": "my_password"
>}
>```

- refreshing JWT-token *(POST)*
>api/v1/jwt/refresh/ 
>```
>{
>    "refresh": "refresh token"
>}
>```

- verifying JWT-token *POST)*
>api/v1/jwt/verify/ 
>```
>{
>    "token": "refresh or access token"
>}
>```

- getting list of all posts *(GET)*
>api/v1/posts/
>>paginate results with the number of posts per page
>>>api/v1/posts/?limit={post_count}
>>>
>>...with starting position of the query in relation to the complete set of unpaginated items
>>>api/v1/posts/?limit={post_count}&offset={start_after}

- create new post. Only "text" field is required *(POST)*
>api/v1/posts/ 
>```
>{
>    "text": "post text",
>    "image": "$binary",
>    "group": integer
>}
>```

- getting, editing or deleting post with id=post_id *(GET, PUT, PATCH, DELETE)*
>api/v1/posts/{post_id}/

- getting list of all groups *(GET)*
>api/v1/groups/

- getting information about group with id=group_id *(GET)*
>api/v1/groups/{group_id}/

- getting list of all post comments with id=post_id *(GET)*
>api/v1/posts/{post_id}/comments/

- create new post comment with id=post_id *(POST)*
>api/v1/posts/{post_id}/comments/
>```
>{
>    "text": "comment text"
>}
>```

- getting, editing or deleting comment with id=comment_id for post with id=post_id *(GET, PUT, PATCH, DELETE)*
>api/v1/posts/{post_id}/comments/{comment_id}/

- getting list of all followings of user who made request *(GET)*
>api/v1/follow/
>>partial match case-insensitive search available *(GET)*
>>
>>api/v1/follow/?search=username
>>

- create new following *(POST)*
>api/v1/follow/
>```
>{
>  "following": "username"
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

https://github.com/NotMainCode

###
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
