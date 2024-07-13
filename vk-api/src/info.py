import json

import requests


def get_permissions(user_id, app_access_token):
    response = requests.get(
        url="https://api.vk.ru/method/account.getAppPermissions",
        params={
            "v": "5.199",
            "access_token": app_access_token,
            "user_id": user_id,
        },
    ).json()
    
    json.dump(response, open("permissions_reponse.json", "w"))
    
    try:
        bit_mask = int(response["response"])
        return decode_permissions(bit_mask)
    except KeyError:
        return {}


def decode_permissions(bit_mask: int):
    access_rights = dict(
        notify=bit_mask & (1 << 0),
        friends=bit_mask & (1 << 1),
        photos=bit_mask & (1 << 2),
        audio=bit_mask & (1 << 3),
        video=bit_mask & (1 << 4),
        stories=bit_mask & (1 << 6),
        pages=bit_mask & (1 << 7),
        menu=bit_mask & (1 << 8),
        status=bit_mask & (1 << 10),
        notes=bit_mask & (1 << 11),
        messages=bit_mask & (1 << 12),
        wall=bit_mask & (1 << 13),
        ads=bit_mask & (1 << 15),
        offline=bit_mask & (1 << 16),
        docs=bit_mask & (1 << 17),
        groups=bit_mask & (1 << 18),
        notifications=bit_mask & (1 << 19),
        stats=bit_mask & (1 << 20),
        email=bit_mask & (1 << 22),
        market=bit_mask & (1 << 27),
        phone_number=bit_mask & (1 << 18),
    )
    for key, val in access_rights.items():
        access_rights[key] = '' if val == 0 else "HELL YEAH"
    return access_rights


def get_account_info(access_token):
    response = requests.get(
        url="https://api.vk.ru/method/account.getInfo",
        params={
            "v": "5.199",
        },
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    ).json()
    json.dump(response, open("account_info_reponse.json", "w"))
    return response