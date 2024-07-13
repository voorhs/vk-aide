import requests


def exhange_silent_token(silent_token: str, uuid, app_service_token: str):
    return requests.get(
        url="https://api.vk.ru/method/auth.exchangeSilentAuthToken",
        params={
            "v": "5.199",
            "access_token": app_service_token,
            "token": silent_token,
            "uuid": [uuid],
        },
    ).json()
