# Setup

- Clone repo and cd into it
```sh
git clone https://github.com/dhruvSHA256/drf-songs && cd drf-songs
```
- Creat a python virtualenv
```sh
python3 -m venv .venv && source ./.venv/bin/activate
```
- Install dependencies
```sh
pip install -r requirements.txt
```
- Cd into project and Run server
```sh
cd songlib
python manage.py runserver
```

# MODEL
## Song
- title
- artist
- album

## User
- email
- username
- password_hash

# API Doc
## Song
- Get all songs ```GET /song/```
- Add new song ```POST /song/```
    - example request:
    ```json
    {
        "title": "title",
        "artist": "artist name",
        "album": "album name"
    }
    ```
- Remove song ``` DELETE /song/ ``` , should require authentication
    - example request:
    ```json
    {
        "title": "title",
    }
    ```
- Update song details ``` PATCH /song/ ``` , should require authentication
    - example request:
    ```json
    {
        "id": "song id",
        "title": "new title",
        "artist": "new artist name",
        "album": "new album name"
    }
    ```
## User
- Get list of all users ``` GET /user/ ```
- Create new user ``` POST /user/ ```
    - example request:
    ```json
    {   
        "email":"cabc@d.com",
        "username":"test",
        "password":"100"
    }
    ```
- Remove a user ``` DELETE /user/ ``` , should require authentication
    - example request:
    ```json
    {
        "email": "email",
    }
    ```
- Update user ``` PATCH /user/ ``` , should require authentication
    - example request:
    ```json
    {
        "id": "userid",
    }
    ```

# TODO
auth
