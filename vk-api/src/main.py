import json
import os
import urllib.parse

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

from .auth import exhange_silent_token
from .info import get_account_info, get_permissions

load_dotenv()
app_service_token = os.environ["APP_SERVICE_TOKEN"]
app_secret_token = os.environ["APP_SECRET_TOKEN"]

app = FastAPI()


@app.get("/")
def get_home_page():
    return HTMLResponse(content=open("static/index.html").read())


@app.get("/vkid_button.js")
def get_index_js():
    return FileResponse(path="static/vkid_button.js")


@app.get("/auth_success")
def auth_success(payload: str, state: str):
    decoded_payload = urllib.parse.unquote(payload)
    payload_dict = json.loads(decoded_payload)
    json.dump(payload_dict, open("payload.json", "w"))

    response = exhange_silent_token(
        silent_token=payload_dict["token"],
        uuid=payload_dict["uuid"],
        app_service_token=app_service_token,
    )
    json.dump(response, open("exchange_reponse.json", "w"))

    response = response["response"]

    info = []
    tokens = [
        app_secret_token,
        app_service_token,
        response["access_token"],
        payload_dict["token"],
    ]
    # info = get_account_info(response['access_token'])
    for tok in tokens:
        # info.append(get_account_info(tok))
        info.append(get_permissions(response["user_id"], tok))
    return {"info": info}
