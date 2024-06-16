import requests


def exhange_silent_token(silent_token: str, uuid, app_access_token: str = "1436970e1436970e1436970e78172e095a114361436970e725f5d29a50d45fa23b72254"):
    return requests.get(
        url='https://api.vk.ru/method/auth.getProfileInfoBySilentToken',
        params={
            'v': "5.199",
            'access_token': app_access_token,
            'token': [silent_token],
            'uuid': [uuid],
            'event': ["click"]
        }
    ).json()
